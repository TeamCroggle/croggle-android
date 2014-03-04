package de.croggle.test;

import android.content.Context;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.backends.headless.HeadlessApplication;
import com.badlogic.gdx.backends.headless.mock.audio.MockAudio;
import com.badlogic.gdx.backends.headless.mock.graphics.MockGraphics;
import com.badlogic.gdx.backends.headless.mock.input.MockInput;

import de.croggle.AlligatorApp;
import de.croggle.backends.AndroidBackendHelper;
import de.croggle.backends.android.AndroidLocalizationBackend;
import de.croggle.data.LocalizationHelper;

public class TestHelper {
	private static Context testContext = null;
	private static AlligatorApp app = null;
	private static AndroidLocalizationBackend localizationBackend = null;
	private static AndroidBackendHelper backendHelper = null;

	private static boolean gdxAppContextChanged = true;
	private static boolean croggleContextChanged = true;
	private static boolean backendContextChanged = true;

	private TestHelper() {
	}

	private static void setupContext(PlatformTestCase test) {
		if (test == null) {
			throw new IllegalArgumentException("Cannot set null as context");
		}
		Context context = test.getContext();

		if (!context.equals(testContext)) {
			System.out.println("New context");
			testContext = context;
			invalidateAll();
		}
	}

	private static void invalidateAll() {
		gdxAppContextChanged = true;
		croggleContextChanged = true;
		backendContextChanged = true;
	}

	public static void setupAll(PlatformTestCase test) {
		setupContext(test);
		setupCroggleBackends(test);
		boolean wasNull = app == null || gdxAppContextChanged;
		setupGdx(test);
		if (wasNull) {
			System.out.println("Create AlligatorApp");
			app.create();
		}
	}

	public static void setupGdx(PlatformTestCase test) {
		setupGdxApp();
		setupGdxAudio();
		setupGdxGraphics();
		setupGdxInput();
	}

	public static void setupGdxApp() {
		if (app == null || gdxAppContextChanged) {
			AlligatorApp.HEADLESS = true;
			app = new AlligatorApp();
			new HeadlessApplication(app); // will automatically register in
											// Gdx.app
		} else if (Gdx.app == null) {
			new HeadlessApplication(app); // will automatically register in
											// Gdx.app
		}
		gdxAppContextChanged = false;
	}

	public static void setupGdxInput() {
		if (Gdx.input == null) {
			Gdx.input = new MockInput();
		}
	}

	public static void setupGdxAudio() {
		if (Gdx.audio == null) {
			Gdx.audio = new MockAudio();
		}
	}

	public static void setupGdxGraphics() {
		if (Gdx.graphics == null) {
			Gdx.graphics = new MockGraphics();
		}
	}

	public static AlligatorApp getApp(PlatformTestCase test) {
		if (app == null || croggleContextChanged) {
			setupAll(test);
		}

		return app;
	}

	public static Context getTestContext() {
		return testContext;
	}

	public static void setupCroggleBackends(PlatformTestCase test) {
		setupContext(test);

		if (localizationBackend == null || backendContextChanged) {
			localizationBackend = new AndroidLocalizationBackend(testContext);
			LocalizationHelper.setBackend(localizationBackend);
			backendContextChanged = false;
		}

		if (backendHelper == null || backendContextChanged) {
			backendHelper = new TestBackendHelper(testContext);
			backendHelper.set();
		}
	}
}
