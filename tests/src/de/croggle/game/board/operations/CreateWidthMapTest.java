package de.croggle.game.board.operations;

import java.util.Map;

import junit.framework.TestCase;

import com.badlogic.gdx.math.Vector2;

import de.croggle.game.Color;
import de.croggle.game.board.Board;
import de.croggle.game.board.BoardObject;
import de.croggle.game.board.ColoredAlligator;
import de.croggle.game.board.Egg;
import de.croggle.game.board.Parent;
import de.croggle.ui.renderer.layout.ActorLayoutConfiguration;
import de.croggle.ui.renderer.layout.TreeGrowth;
import de.croggle.util.convert.LambdaToAlligator;

public class CreateWidthMapTest extends TestCase {
	public void testSimple() {
		Board b = new Board();
		ColoredAlligator a = new ColoredAlligator(true, true, new Color(0),
				true);
		b.addChild(a);
		Egg e1 = new Egg(true, true, new Color(0), true);
		a.addChild(e1);
		Egg e2 = new Egg(true, true, new Color(1), true);
		b.addChild(e2);

		Map<BoardObject, Float> map = CreateWidthMap.create(b);
		assertEquals(2.0f, map.get(b));
		assertEquals(1.0f, map.get(a));
		assertEquals(1.0f, map.get(e1));
		assertEquals(1.0f, map.get(e2));
	}

	public void testCase0() {
		// standard layout options
		final float w = 150;
		final float s = 0.75f;
		final float p = 2;
		ActorLayoutConfiguration config = new ActorLayoutConfiguration(
				new Vector2(0, 0), TreeGrowth.NEG_POS, TreeGrowth.POS_NEG,
				TreeGrowth.NEG_POS, TreeGrowth.NEG_POS, s, p, p, null, false,
				w, w, w, w, w, w);

		Board b = LambdaToAlligator.convert("(λx.x) ((λy.y) (λz.z))");
		Map<BoardObject, Float> map = CreateWidthMap.create(b,
				config.getUniformObjectWidth(),
				config.getVerticalScaleFactor(), config.getHorizontalPadding());
		float expected = Math.max(w, w * s) + p
				+ Math.max(w, 2 * Math.max(w * s, w * s * s) + p * s);
		assertEquals(expected, map.get(b), 1e-8);
		expected = Math.max(w, 2 * Math.max(w * s, w * s * s) + p * s);
		assertEquals(expected, map.get(b.getChildAtPosition(1)), 1e-8);
		expected = Math.max(w, w * s);
		assertEquals(expected, map.get(b.getChildAtPosition(0)), 1e-8);
		expected = w * s;
		assertEquals(expected, map.get(((Parent) b.getChildAtPosition(0))
				.getChildAtPosition(0)), 1e-8);
	}

	public void testCaseNoScaling() {
		Board b = LambdaToAlligator.convert("(λx.x) ((λy.y) (λz.z))");
		Map<BoardObject, Float> map = CreateWidthMap.create(b, 1, 1, 0);
		assertEquals(3.f, map.get(b), 1e-8);
		assertEquals(1.f, map.get(b.getChildAtPosition(0)), 1e-8);
	}
}
