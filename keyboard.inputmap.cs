////////////////////////////////////////////////
//// Keyboard mappings
// arrows
//moveMap.bind(keyboard, w, accelerate);
//moveMap.bind(keyboard, s, brake);
//moveMap.bind(keyboard, a, steer_left);
//moveMap.bind(keyboard, d, steer_right);

moveMap.bind( keyboard, a, moveleft );
moveMap.bind( keyboard, d, moveright );
moveMap.bind( keyboard, w, moveforward );
moveMap.bind( keyboard, s, movebackward );

moveMap.bind( keyboard, a, steer_left );
moveMap.bind( keyboard, d, steer_right );
moveMap.bind( keyboard, w, accelerate );
moveMap.bind( keyboard, s, brake );

// shifting
moveMap.bind( keyboard, lshift, clutch );
moveMap.bind( keyboard, x, shiftUp);
moveMap.bind( keyboard, z, shiftDown);
moveMap.bind( keyboard, q, toggleShifterMode );

$np_movespeed = 0.1;
// camera/numpad
function np_x(%val)
{
   if(%val > 0)
   {
      $mvYawLeftSpeed = %val * $np_movespeed;
      $mvYawRightSpeed = 0;
   }
   else
   {
      $mvYawLeftSpeed = 0;
      $mvYawRightSpeed = -%val * $np_movespeed;
   }
}
function np_y(%val)
{
   if(%val > 0)
   {
      $mvPitchDownSpeed = %val * $np_movespeed;
      $mvPitchUpSpeed = 0;
   }
   else
   {
      $mvPitchDownSpeed = 0;
      $mvPitchUpSpeed = -%val * $np_movespeed;
   }
}
moveMap.bindCmd(keyboard, numpad4, "np_x(-1);", "np_x(0);");
moveMap.bindCmd(keyboard, numpad6, "np_x(1);", "np_x(0);");
moveMap.bindCmd(keyboard, numpad8, "np_y(-1);", "np_y(0);");
moveMap.bindCmd(keyboard, numpad2, "np_y(1);", "np_y(0);");
moveMap.bindCmd(keyboard, numpad9, "gamepadZoom(-0.1);", "gamepadZoom(0);");
moveMap.bindCmd(keyboard, numpad3, "gamepadZoom(0.1);", "gamepadZoom(0);");
moveMap.bindCmd(keyboard, numpad5, "beamNGResetCamera();", "");
moveMap.bindCmd(keyboard, numpad1, "beamNGCameraLookback();", "");
moveMap.bindCmd(keyboard, tab,     "beamNGSwitchVehicle(1);", "");
moveMap.bindCmd(keyboard, "shift tab", "beamNGSwitchVehicle(-1);", "");
moveMap.bindCmd(keyboard, c,       "beamNGCameraToggle();", "");
moveMap.bindCmd(keyboard, "ctrl m", "reloadInputMaps();", "" );

// assorted
moveMap.bindCmd(keyboard, i, "beamNGResetPhysics();", "");
moveMap.bindCmd(keyboard, r, "beamNGResetPhysics();", "");
moveMap.bindCmd(keyboard, j, "beamNGTogglePhysics();", "");
moveMap.bind(keyboard, space, parkingbrake_toggle);
moveMap.bindCmd(keyboard, "r", "beamNGReloadCurrentVehicle();", "");
moveMap.bindCmd(keyboard, "shift t", "beamNGReloadSystemLua();", "");
moveMap.bindSLuaCmd(keyboard, "ctrl t", "showAIGUI()", "");

moveMap.bindCmd(keyboard, "e", "Canvas.pushDialog(VehicleChooser);", "");
moveMap.bindVLuaCmd(keyboard, "q", "partmgmt.showGUI()", "");


moveMap.bindCmd(keyboard, "ctrl escape", "quit();", "" );
moveMap.bindCmd(keyboard, "escape", "", "handleEscape();");

// some toolkit functions
moveMap.bindVLuaCmd(keyboard, "k", "bdebug.setMode('-1')", "");
moveMap.bindVLuaCmd(keyboard, "ctrl k", "bdebug.toggleMeshAlpha(-1)", "");
moveMap.bindVLuaCmd(keyboard, "l", "bdebug.setMode('+1')", "");
moveMap.bindVLuaCmd(keyboard, "ctrl l", "bdebug.toggleMeshAlpha(1)", "");


moveMap.bindVLuaCmd(keyboard, "comma", "electrics.toggle_left_signal()", "");
moveMap.bindVLuaCmd(keyboard, "period", "electrics.toggle_right_signal()", "");
moveMap.bindVLuaCmd(keyboard, "slash", "electrics.toggle_warn_signal()", "");
moveMap.bindVLuaCmd(keyboard, "n", "electrics.toggle_lights()", "");
moveMap.bindVLuaCmd(keyboard, "shift b", "input.toggleDynamicSteering()", "");


moveMap.bindCmd(keyboard, "f1", "BeamNGHelp.toggle();", "");

moveMap.bindVLuaCmd(keyboard, "alt f1", "bdebug.setMode(0)", "");
moveMap.bindVLuaCmd(keyboard, "shift f1", "bdebug.setMode(1)", "");
moveMap.bindVLuaCmd(keyboard, "shift f2", "bdebug.setMode(2)", "");
moveMap.bindVLuaCmd(keyboard, "shift f3", "bdebug.setMode(3)", "");
moveMap.bindVLuaCmd(keyboard, "shift f4", "bdebug.setMode(4)", "");
moveMap.bindVLuaCmd(keyboard, "shift f5", "bdebug.setMode(5)", "");
moveMap.bindVLuaCmd(keyboard, "shift f6", "bdebug.setMode(6)", "");
moveMap.bindVLuaCmd(keyboard, "shift f7", "bdebug.setMode(7)", "");
moveMap.bindVLuaCmd(keyboard, "shift f8", "bdebug.setMode(8)", "");

moveMap.bindVLuaCmd(keyboard, "left", "bullettime.set('-20')", "");
moveMap.bindVLuaCmd(keyboard, "right", "bullettime.set('+20')", "");
moveMap.bindVLuaCmd(keyboard, "up", "bullettime.set(100)", "");
moveMap.bindVLuaCmd(keyboard, "down", "bullettime.set(5)", "");
