package de.croggle.game.board.operations;

import junit.framework.TestCase;
import de.croggle.game.board.Board;
import de.croggle.util.convert.AlligatorToLambda;
import de.croggle.util.convert.LambdaToAlligator;

public class RemoveNeedlessAgedAlligatorsTest extends TestCase {
	public void testLeftmost() {
		// λ
		String term = "(x x)";
		Board b = LambdaToAlligator.convert(term);
		RemoveNeedlessAgedAlligators.remove(b, null);
		assertEquals("x x", AlligatorToLambda.convert(b));
	}

	public void testMiddle() {
		String term = "x (x x) x";
		Board b = LambdaToAlligator.convert(term);
		RemoveNeedlessAgedAlligators.remove(b, null);
		assertEquals("x x x x", AlligatorToLambda.convert(b));
	}

	public void testAbstracted() {
		String term = "λx.(x x)";
		Board b = LambdaToAlligator.convert(term);
		RemoveNeedlessAgedAlligators.remove(b, null);
		assertEquals("λx.x x", AlligatorToLambda.convert(b));
	}

	public void testNoChange() {
		String term = "λx.x (x x)";
		Board b = LambdaToAlligator.convert(term);
		RemoveNeedlessAgedAlligators.remove(b, null);
		assertEquals("λx.x (x x)", AlligatorToLambda.convert(b));
	}

	public void testCase0() {
		String term = "λx.y (x x)";
		Board b = LambdaToAlligator.convert(term);
		RemoveNeedlessAgedAlligators.remove(b, null);
		assertEquals("λx.y x x", AlligatorToLambda.convert(b));
	}
}
