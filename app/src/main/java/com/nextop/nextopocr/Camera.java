package com.nextop.nextopocr;

import android.content.Context;
import android.graphics.Rect;
import android.view.SurfaceHolder;
import android.view.SurfaceView;

public class Camera implements SurfaceHolder.Callback{

    private SurfaceView mCameraView

    public final class CameraManager {

        private static final String TAG = CameraManager.class.getSimpleName();

        private static final int MIN_FRAME_WIDTH = 50;
        private static final int MIN_FRAME_HEIGHT = 20;
        private static final int MAX_FRAME_WIDTH = 800;
        private static final int MAX_FRAME_HEIGHT = 600;

        private final Context context;
        private final CameraConfigurationManager configManager;
        private android.hardware.Camera camera;
        private AutoFocusManager autoFocusManager;
        private Rect framingRect;
        private Rect framingRectInPreview;
        private boolean initialized;
        private boolean previewing;
        private boolean reverseImage;
        private int requestedFramingRectWidth;
        private int requestedFramingRectHeight;



}
