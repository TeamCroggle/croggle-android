package de.croggle.backends;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import android.content.Context;

import com.badlogic.gdx.Application;
import com.badlogic.gdx.Gdx;

import de.croggle.backends.android.AndroidContentValues;
import de.croggle.backends.android.AndroidDatabaseHelper;
import de.croggle.backends.sqlite.ContentValues;
import de.croggle.backends.sqlite.DatabaseHelper;

/**
 * A class to help with additional capabilities of the different backends,
 * without directly referencing them (using reflection). By doing so, the helper
 * can be part of every platform's build without pulling in dependencies to the
 * different backends.
 * 
 * The class's methods degrade gracefully, meaning that they silently ignore if
 * a certain functionality is currently unavailable.
 */
public class AndroidBackendHelper extends BackendHelper {
	public AndroidBackendHelper() {
	}

	private static Object getWakeLock() {
		Application app = Gdx.app;
		Method getWakeLock = null;
		try {
			getWakeLock = app.getClass().getMethod("getWakeLock");
		} catch (NoSuchMethodException e) {
		}
		if (getWakeLock != null) {
			try {
				return getWakeLock.invoke(app);
			} catch (IllegalAccessException e) {
				return null;
			} catch (InvocationTargetException e) {
				return null;
			} catch (IllegalArgumentException e) {
				return null;
			}
		} else {
			return null;
		}
	}

	public static Context getAndroidContext() {
		return ((AndroidBackendHelper) backend).getContext();
	}

	@Override
	protected boolean wakelockAcquire() {
		Object wakeLock = getWakeLock();
		if (wakeLock != null) {
			Method acquire = null;
			try {
				acquire = wakeLock.getClass().getMethod("acquire");
			} catch (NoSuchMethodException e) {
			}
			if (acquire != null) {
				try {
					acquire.invoke(wakeLock);
					return true;
				} catch (IllegalAccessException e) {
				} catch (IllegalArgumentException e) {
				} catch (InvocationTargetException e) {
				}
			}
		}
		return false;
	}

	@Override
	protected boolean wakelockRelease() {
		Object wakeLock = getWakeLock();
		if (wakeLock != null) {
			Method release = null;
			try {
				release = wakeLock.getClass().getMethod("release");
			} catch (NoSuchMethodException e) {
			}
			if (release != null) {
				try {
					release.invoke(wakeLock);
					return true;
				} catch (IllegalAccessException e) {
				} catch (IllegalArgumentException e) {
				} catch (InvocationTargetException e) {
				}
			}
		}
		return false;
	}

	@Override
	protected DatabaseHelper instantiateDatabaseHelper() {
		return new AndroidDatabaseHelper(getAndroidContext());
	}

	@Override
	protected ContentValues instantiateContentValues() {
		return new AndroidContentValues();
	}

	@Override
	protected String assetDirPath() {
		return "";
	}

	protected Context getContext() {
		return (Context) Gdx.app;
	}
}
