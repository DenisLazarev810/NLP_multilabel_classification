import static org.junit.Assert.*;

import org.junit.Test;


public class BankTest {
	private static final double DELTA = 1e-10;
	private static final int HashTop = 999999;

	@Test
	public void testCreate() {
		int i,j,k,l,m;
		i = Bank.create("USD");
		j = Bank.create("RUB");
		k = Bank.create("EURO");
		l = Bank.create("RUB");
		m = Bank.create("EURO");
		assertEquals (HashSetExample.findcurrency(i), "USD");
		assertEquals (HashSetExample.findcurrency(k), "EURO");
		assertEquals (HashSetExample.findcurrency(m), "EURO");
		assertEquals (HashSetExample.findsum(j),0.0,DELTA);
		assertEquals (HashSetExample.findsum(l),0.0,DELTA);		
		
		
	}

	@Test
	public void testAdd() {
		int i,j,k,l,m;
		i = Bank.create("USD");
		j = Bank.create("RUB");
		k = Bank.create("EURO");
		l = Bank.create("RUB");
		m = Bank.create("EURO");
		Bank.add(i,"EURO",2.0);//кладём 2 евро на доллпровую карту
		assertEquals (HashSetExample.findsum(i)*Currency.USD,2*Currency.EURO,DELTA);
		Bank.add(j,"USD",3.0);//кладём 3 доларя на рублёвую карту
		assertEquals (HashSetExample.findsum(j)*Currency.USD,3*Currency.RUB,DELTA);
		Bank.add(k,"RUB",4.0);//кладём рубля на долларовую карту
		assertEquals (HashSetExample.findsum(k)*Currency.EURO,4*Currency.RUB,DELTA);
		
		
	}
	
	
	
	@Test
	public void testBalanc() {
		int i,j,k,l,m;
		i = Bank.create("USD");
		j = Bank.create("RUB");
		k = Bank.create("EURO");
		l = Bank.create("RUB");
		m = Bank.create("EURO");
		Bank.add(i,"EURO",2.0);//кладём 2 евро на доллпровую карту
		Bank.add(j,"USD",3.0);//кладём 3 доларя на рублёвую карту
		Bank.add(k,"RUB",4.0);//кладём рубля на долларовую карту
		assertEquals(Bank.balanc(i, "USD"), 2.0*Currency.USD/Currency.EURO, DELTA);
		assertEquals(Bank.balanc(j, "RUB"), 3.0*Currency.USD/Currency.RUB, DELTA);
		assertEquals(Bank.balanc(k, "EURO"), 4.0*Currency.RUB/Currency.EURO, DELTA);
	}
	
	
	@Test
	public void testMoneyMove() {
		int i,j,k,l,m;
		i = Bank.create("USD");
		j = Bank.create("RUB");
		k = Bank.create("EURO");
		l = Bank.create("RUB");
		m = Bank.create("EURO");
		Bank.add(i,"USD",2.5);
		Bank.add(j,"RUB",3.0);
		Bank.add(k,"EURO",4.0);//всюду кладём родную валюту
		Bank.moneymove(i, j, "USD", 1);
		Bank.moneymove(i, k, "USD", 1);
		assertEquals(Bank.balanc(j, "RUB"), 3.0 + Currency.USD, DELTA);
		assertEquals(Bank.balanc(i, "RUB"), 0.5*Currency.USD, DELTA);
		assertEquals(Bank.balanc(k, "EURO"), 4.0 + Currency.USD/Currency.EURO, DELTA);
		
		
		
	}
	
	
}