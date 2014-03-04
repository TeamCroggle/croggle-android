package de.croggle.test;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import de.croggle.backends.android.AndroidDatabase;
import de.croggle.backends.android.AndroidDatabaseHelper;

public class TestDatabaseHelper extends AndroidDatabaseHelper {

	public static final String TEST_DB_NAME = "testDB";

	public TestDatabaseHelper(Context context) {
		super(context);
	}

	@Override
	protected SQLiteOpenHelper instantiateHelper(Context context) {
		return new Helper(context);
	}

	private class Helper extends SQLiteOpenHelper {
		public Helper(Context context) {
			super(context, TEST_DB_NAME, null, DATABASE_Version);
			// TODO Auto-generated constructor stub
		}

		@Override
		public void onCreate(SQLiteDatabase db) {
			TestDatabaseHelper.this.onCreate(new AndroidDatabase(db));
		}

		@Override
		public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
			TestDatabaseHelper.this.onUpgrade(new AndroidDatabase(db),
					oldVersion, newVersion);
		}
	}
}
