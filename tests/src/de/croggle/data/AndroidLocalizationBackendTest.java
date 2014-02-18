package de.croggle.data;

import static de.croggle.data.LocalizationHelper._;

import java.util.Locale;

import android.test.InstrumentationTestCase;
import de.croggle.backends.LocalizationBackend;
import de.croggle.backends.android.AndroidLocalizationBackend;

public class AndroidLocalizationBackendTest extends InstrumentationTestCase {

	@Override
	public void setUp() {
		LocalizationBackend locBack = new AndroidLocalizationBackend(
				getInstrumentation().getContext());
		LocalizationHelper.setBackend(locBack);
		LocalizationHelper.setApplicationLocale(LocalizationHelper
				.getSystemLocale());
	}

	public void testAppName() {
		String expected = "Croggle Test";
		String actual = _("app_name");

		assertEquals(expected, actual);
	}

	public void testPluralMissing() {
		String key = "app_name";
		String actual = _(key, 3);

		assertEquals(key, actual);
	}

	public void testSetGetLocale() {
		Locale l1 = Locale.GERMANY;
		Locale l2 = Locale.UK;

		LocalizationHelper.setApplicationLocale(l1);
		LocalizationHelper.setApplicationLocale(l2);
		assertEquals(l2, LocalizationHelper.getApplicationLocale());
	}

	public void testSystemLocale() {
		Locale sys = LocalizationHelper.getSystemLocale();
		// system locale should be default
		assertEquals(sys, LocalizationHelper.getApplicationLocale());
	}
}
