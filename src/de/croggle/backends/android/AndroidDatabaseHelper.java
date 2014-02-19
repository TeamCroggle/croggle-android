package de.croggle.backends.android;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import de.croggle.backends.sqlite.Database;
import de.croggle.backends.sqlite.DatabaseHelper;

public class AndroidDatabaseHelper extends DatabaseHelper {
	private final Helper helper;

	/**
	 * Creates a new DatabaseHelper which is used for managing the database.
	 * 
	 * @param context
	 *            the context used to create the database
	 */
	public AndroidDatabaseHelper(Context context) {
		helper = new Helper(context);
	}

	@Override
	public Database getWritableDatabase() {
		return new AndroidDatabase(helper.getWritableDatabase());
	}

	@Override
	public void close() {
		helper.close();
	}

	private class Helper extends SQLiteOpenHelper {
		public Helper(Context context) {
			super(context, DATABASE_NAME, null, DATABASE_Version);
			// TODO Auto-generated constructor stub
		}

		@Override
		public void onCreate(SQLiteDatabase db) {
			AndroidDatabaseHelper.this.onCreate(new AndroidDatabase(db));
		}

		@Override
		public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
			AndroidDatabaseHelper.this.onUpgrade(new AndroidDatabase(db),
					oldVersion, newVersion);
		}
	}
}
