package de.croggle.test;

import android.content.Context;
import de.croggle.backends.AndroidBackendHelper;
import de.croggle.backends.sqlite.DatabaseHelper;

public class TestBackendHelper extends AndroidBackendHelper {

	private final Context context;

	public TestBackendHelper(Context ctxt) {
		context = ctxt;
	}

	@Override
	public Context getContext() {
		return context;
	}

	@Override
	protected DatabaseHelper instantiateDatabaseHelper() {
		return new TestDatabaseHelper(context);
	}
}
