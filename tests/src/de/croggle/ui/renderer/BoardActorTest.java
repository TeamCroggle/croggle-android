package de.croggle.ui.renderer;

import de.croggle.game.ColorController;
import de.croggle.game.ColorOverflowException;
import de.croggle.game.Simulator;
import de.croggle.game.board.AlligatorOverflowException;
import de.croggle.game.board.Board;
import de.croggle.game.board.IllegalBoardException;
import de.croggle.game.event.BoardEventMessenger;
import de.croggle.test.PlatformTestCase;
import de.croggle.test.TestHelper;
import de.croggle.ui.renderer.layout.ActorLayoutConfiguration;
import de.croggle.ui.renderer.objectactors.BoardObjectActorFactory;
import de.croggle.util.convert.LambdaToAlligator;

public class BoardActorTest extends PlatformTestCase {
	@Override
	public void setUp() {
		TestHelper.setupCroggleBackends(this);
	}

	public void testStackoverflowIssue() {
		try {
			BoardEventMessenger messenger = new BoardEventMessenger();
			Board board = LambdaToAlligator
					.convert("λg.(λx.g (x x)) (λx.g (x x))");
			ColorController ccontroller = new ColorController();
			Simulator sim = new Simulator(board, ccontroller, messenger);
			ActorLayoutConfiguration config = new ActorLayoutConfiguration();
			config.setColorController(ccontroller);
			BoardObjectActorFactory.setActorsHeadless(true);
			BoardActor.setHeadlessInstantiation(true);
			BoardActor ba = new BoardActor(sim.getCurrentBoard(), config);
			messenger.register(ba.getBoardEventListener());
			while (true) {
				try {
					sim.evaluate();
				} catch (ColorOverflowException e) {
					fail("Colors are NOT supposed to overflow");
				} catch (AlligatorOverflowException e) {
					// Alligators are supposed to overflow
					return;
				}
			}
		} catch (IllegalBoardException e) {
			fail("Board should not have errors");
		}
	}
}
