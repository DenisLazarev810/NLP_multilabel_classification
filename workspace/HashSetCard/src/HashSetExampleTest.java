import static org.junit.Assert.*;

import org.junit.Test;


public class HashSetExampleTest {
	private static final int HashTop = 999999;
	private static final double DELTA = 1e-10;

	@Test
	public void testFindsum() {
		Card card = new Card();
		card.id = HashTop;
		card.sum = 2.0;
		card.currency = "USD";
		HashSetExample.add(card);
		assertEquals(HashSetExample.findsum(HashTop),2.0,DELTA);
		
		
	}
	
	@Test
	public void testFindcurrency() {
		Card card = new Card();
		card.id = HashTop;
		card.sum = 2.0;
		card.currency = "USD";
		HashSetExample.add(card);
		assertEquals(HashSetExample.findcurrency(HashTop),"USD");
		
		
	}

}
