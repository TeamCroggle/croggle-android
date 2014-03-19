package de.croggle.game.board.operations;

import junit.framework.TestCase;
import de.croggle.game.Color;
import de.croggle.game.board.Board;
import de.croggle.game.board.ColoredAlligator;
import de.croggle.game.board.Egg;

public class CopyConstellationTest extends TestCase {
	public void testSimpleConstellation() {
		Board b = new Board();
		ColoredAlligator a1 = new ColoredAlligator(true, true,
				Color.uncolored(), true);
		Egg e11 = new Egg(true, true, Color.uncolored(), true);
		Egg e12 = new Egg(true, true, Color.uncolored(), true);
		Egg e2 = new Egg(true, true, Color.uncolored(), true);
		b.addChild(a1);
		a1.addChild(e11);
		a1.addChild(e12);
		b.addChild(e2);

		Board b_copy = CopyConstellation.copy(b);
		assertTrue(b.match(b_copy));
	}
}
