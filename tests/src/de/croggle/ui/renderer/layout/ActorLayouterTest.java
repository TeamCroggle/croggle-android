package de.croggle.ui.renderer.layout;

import junit.framework.TestCase;
import de.croggle.game.ColorController;
import de.croggle.game.ColorOverflowException;
import de.croggle.game.Simulator;
import de.croggle.game.board.AlligatorOverflowException;
import de.croggle.game.board.Board;
import de.croggle.game.board.IllegalBoardException;
import de.croggle.ui.renderer.objectactors.BoardObjectActorFactory;
import de.croggle.util.convert.LambdaToAlligator;

public class ActorLayouterTest extends TestCase {

	public void testLayouterSpeed() {
		ActorLayoutConfiguration config = new ActorLayoutConfiguration();
		config.setColorController(new ColorController());
		BoardObjectActorFactory.setActorsHeadless(true);
		Board bigBoard = createHugeBoard();
		long timeBefore = System.currentTimeMillis();
		ActorLayout layout = ActorLayout.create(bigBoard, config);
		long timeAfter = System.currentTimeMillis();
		System.out
				.println("Time to create: " + (timeAfter - timeBefore) + "ms");
		timeBefore = System.currentTimeMillis();
		layout.getDeltasToFix();
		timeAfter = System.currentTimeMillis();
		System.out.println("Time to fix nothing: " + (timeAfter - timeBefore)
				+ "ms");
		bigBoard.removeChild(bigBoard.getFirstChild());
		timeBefore = System.currentTimeMillis();
		layout.getDeltasToFix();
		timeAfter = System.currentTimeMillis();
		System.out.println("Time to delete almost everything: "
				+ (timeAfter - timeBefore) + "ms");
	}

	private Board createHugeBoard() {
		Board board = LambdaToAlligator.convert("λg.(λx.g (x x)) (λx.g (x x))");
		ColorController ccontroller = new ColorController();
		try {
			Simulator sim = new Simulator(board, ccontroller, null);
			try {
				while (true) {
					sim.evaluate();
				}
			} catch (ColorOverflowException e) {
				fail("Colors are NOT supposed to overflow");
			} catch (AlligatorOverflowException e) {
				return sim.getCurrentBoard();
			}
		} catch (IllegalBoardException e) {
			fail("Board should not have errors");
		}
		// cannot happen
		return null;
	}
}
