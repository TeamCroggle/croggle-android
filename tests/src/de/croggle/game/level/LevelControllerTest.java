package de.croggle.game.level;

import junit.framework.Assert;
import de.croggle.AlligatorApp;
import de.croggle.test.PlatformTestCase;
import de.croggle.test.TestHelper;

public class LevelControllerTest extends PlatformTestCase {

	LevelController controller;

	@Override
	protected void setUp() throws Exception {
		AlligatorApp app = TestHelper.getApp(this);
		controller = new LevelController(0, app);
	}

	public void testSize() {
		assertTrue(controller.getPackageSize() == 12);
	}

	public void testLevel() {
		Assert.assertTrue(controller
				.getLevel(0)
				.getDescription()
				.equals("Erstes Tutorial Level in dem das Einfärben von Spielelementen erklärt wird."));
	}

}
