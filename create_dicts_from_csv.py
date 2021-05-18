"""
Prepare all required data.
"""

import pandas as pd
import csv


def merge_csv_columns( input_name, output_name ):
    f1 = open(input_name, 'r') # входной csv-файл
    #f2 = open(input_name_1, 'r') # входной csv-файл
    f2 = open(output_name, 'w') # выходной csv-файл
    
    reader = csv.reader(f1 )#, delimiter=' ', quotechar='|')
    writer = csv.writer( f2 )
    i = 0
    for row in reader:
        if i > 0:
            #print( row[0], type( row[0] ), row[3], type( row[3] )  )
            row[3] = row[2] + '. \n' + row[3]
            #print( row[0], type( row[0] ), row[3], type( row[3] )  ) # объединим заголовок с файлом
            
            new_rows = []
            for i in range( len( row ) ):
                new_rows += [ row[i] ]
            
            writer.writerow( new_rows )
        else:
            writer.writerow( row )
 
        i += 1

    f1.close()
    f2.close()
    #f3.close()

def merge_tables( name_1, name_2, output ):
    f1 = open(name_1, 'r') # входной csv-файл
    f2 = open(name_2, 'r') # входной csv-файл
    f3 = open(output, 'w') # выходной csv-файл
    
    reader_1 = csv.reader(f1 )#, delimiter=' ', quotechar='|')
    reader_2 = csv.reader(f2 )#, delimiter=' ', quotechar='|')
    writer = csv.writer( f3 )
    
    i = 0
    for row in reader_1:
        if i >= 0:
            writer.writerow( row )
        i += 1

    i = 0
    for row in reader_2: 
        if i > 0:
            writer.writerow( row )
        i += 1

    f1.close()
    f2.close()
    f3.close()


def drop_parts( input_name, output_name ):
    f1 = open(input_name, 'r') # входной csv-файл
    #f2 = open(input_name_1, 'r') # входной csv-файл
    f2 = open(output_name, 'w') # выходной csv-файл
    
    reader = csv.reader(f1 )#, delimiter=' ', quotechar='|')
    writer = csv.writer( f2 )
    i = 0
    writer.writerow( [ 'text' ] )
    for row in reader:
        if i >= 0:
            new_rows = [row[3]]
            writer.writerow( new_rows )
 
        i += 1

    f1.close()
    f2.close()


input_name = 'data/test_data.csv'
output_name = 'data/test_new.csv'
merge_csv_columns( input_name, output_name )

input_name = 'data/train_data.csv'
output_name = 'data/train_new.csv'
merge_csv_columns( input_name, output_name )

name_1 = 'data/train_new.csv'
name_2 = 'data/test_new.csv'
output = 'data/merged.csv'
merge_tables( name_1, name_2, output )

input_name = 'data/merged.csv'
output_name = 'data/pretrain.csv'

drop_parts( input_name, output_name )


DATA_PATH = 'data/pretrain.csv'

train = pd.read_csv(DATA_PATH)

# запишем данные в txt-файл
with open('data/item_name.txt', 'w') as f:
    f1 = open(DATA_PATH, 'r') # входной csv-файл
    #f2 = open(input_name_1, 'r') # входной csv-файл
    
    reader = csv.reader(f1 )#, delimiter=' ', quotechar='|')
    i = 0
    for row in reader:
        f.writelines(row[0] + '\n')


# prepare data for training language model
#item_names = train.drop_duplicates()
#item_names = item_names.map(lambda x: str(x) + '\n')

#with open('data/item_name_2000.txt', 'w') as f:
#    f.writelines(item_names[:2000].to_string())
#with open('data/item_name_1500.txt', 'w') as f:
#    f.writelines(item_names[:1500].to_string())
#with open('data/item_name_1000.txt', 'w') as f:
#    f.writelines(item_names[:1000].to_string())
#with open('data/item_name.txt', 'w') as f:
#    f.writelines(item_names.to_string())

# prepare training data
#train2 = train[train.category_id != -1].drop_duplicates('text')
#train2 = train2[train2.item_name != '']
#train2.to_csv('data/train_data.csv', index=False)

# prepare list of categories
#categories = sorted(train2.category_id.unique())
#categories = pd.Series(categories, name='category')
#categories.to_csv('data/categories.csv', index=False)
