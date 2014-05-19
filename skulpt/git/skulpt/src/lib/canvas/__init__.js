var listeImages = new Array();
var image_count;

var fontfaces = {
        'serif': true,
        'sans-serif': true,
        'monospace': true
    };

var truncate = function (number) {
        return Math[number < 0 ? 'ceil' : 'floor'](number);
    };

var cancelAnimation = function (frame) {
            if (animationID) {
                animationID = null;
            };
};


var checkPoint = function (point) { // Check that it is a two element sequence
        if (!Sk.builtin.checkSequence(point) || point.sq$length() != 2) {
            return false;
        };
        // Check that each element is a number
        if (!Sk.builtin.checkNumber(point.mp$subscript(0)) || !Sk.builtin.checkNumber(point.mp$subscript(1))) {
            return false;
        };
        return true;
    };

var $builtinmodule = function(name)
{
    var mod = {};
	var timers = [];
    var sounds = [];
	 var sound = function ($gbl, $loc) {
        $loc.__init__ = new Sk.builtin.func(function (self, sound_file) {
            if (Sk.builtin.checkString(sound_file)) {
                sound_file = Sk.ffi.unwrapo(sound_file);
            }
            self.sound = new Audio(sound_file);
            self.__class__ = mod.Sound;
            // Store sound
            sounds.push(self);
        });
        $loc.set_volume = new Sk.builtin.func(function (self, vol) {
            Sk.builtin.pyCheckArgs("set_volume", arguments, 2, 2);
            if (!Sk.builtin.checkNumber(vol)) {
                throw new Sk.builtin.TypeError("Volume must be a number");
            };
            vol = Sk.builtin.asnum$(vol);
            if ((vol >= 0) && (vol <= 1)) {
                self.sound.volume = vol;
            } else {
                throw new Sk.builtin.ValueError("Volume must be between 0 and 1");
            };
            return Sk.builtin.none.none$;
        });
        // $loc.wait = new Sk.builtin.func(function(self) {        // });
        $loc.play = new Sk.builtin.func(function (self) {
            Sk.builtin.pyCheckArgs("play", arguments, 1, 1);
            self.sound.play();
            return Sk.builtin.none.none$;
        });
        $loc.pause = new Sk.builtin.func(function (self) {
            Sk.builtin.pyCheckArgs("pause", arguments, 1, 1);
            self.sound.pause();
            return Sk.builtin.none.none$;
        });
        $loc.rewind = new Sk.builtin.func(function (self) {
            Sk.builtin.pyCheckArgs("rewind", arguments, 1, 1);
            self.sound.pause();
            if (self.sound.currentTime) {
                self.sound.currentTime = 0;
            };
            return Sk.builtin.none.none$;
        });
    };
    mod.Sound = Sk.misceval.buildClass(mod, sound, 'Sound', []);
    mod.load_sound = new Sk.builtin.func(function (sound_file) {
        Sk.builtin.pyCheckArgs("load_image", arguments, 1, 1);
        if (!Sk.builtin.checkString(sound_file)) {
            throw new Sk.builtin.TypeError("expected string");
        };
        return Sk.misceval.callsim(mod.Sound, sound_file);
    });
	
	var image = function ($gbl, $loc) {
        $loc.__init__ = new Sk.builtin.func(function (self, image_file) {
            self.image = new Image();
            self.image.src = Sk.ffi.unwrapo(image_file);
            self.__class__ = mod.Image;
        });
        // $loc.wait = new Sk.builtin.func(function(self) {        // });
        $loc.get_width = new Sk.builtin.func(function (self) {
            Sk.builtin.pyCheckArgs("get_width", arguments, 1, 1);
            return Sk.builtin.assk$(self.image.width, Sk.builtin.nmber.int$);
        });
        $loc.get_height = new Sk.builtin.func(function (self) {
            Sk.builtin.pyCheckArgs("get_height", arguments, 1, 1);
            return Sk.builtin.assk$(self.image.height, Sk.builtin.nmber.int$);
        });
    };
    mod.Image = Sk.misceval.buildClass(mod, image, 'Image', []);
    
var control = function ($gbl, $loc) {
        $loc.__init__ = new Sk.builtin.func(function (self, object) {
            self._object = object;
        });
        $loc.get_text = new Sk.builtin.func(function (self) {
            Sk.builtin.pyCheckArgs("get_text", arguments, 1, 1);
            return Sk.ffi.basicwrap(self._object.textContent);
        });
        $loc.set_text = new Sk.builtin.func(function (self, text) {
            Sk.builtin.pyCheckArgs("set_text", arguments, 2, 2);
            var s = new Sk.builtin.str(text);
            self._object.textContent = Sk.ffi.unwrapo(s);
        });
    };
    mod.Control = Sk.misceval.buildClass(mod, control, 'Control', []);
    // Text Area Control class
    var textareacontrol = function ($gbl, $loc) {
        $loc.__init__ = new Sk.builtin.func(function (self, object) {
            self._object = object;
        });
        $loc.get_text = new Sk.builtin.func(function (self) {
            Sk.builtin.pyCheckArgs("get_text", arguments, 1, 1);
            return Sk.ffi.basicwrap(self._object.value);
        });
        $loc.set_text = new Sk.builtin.func(function (self, text) {
            Sk.builtin.pyCheckArgs("set_text", arguments, 2, 2);
            var s = new Sk.builtin.str(text);
            self._object.value = Sk.ffi.unwrapo(s);
        });
    };
    mod.TextAreaControl = Sk.misceval.buildClass(mod, textareacontrol, 'TextAreaControl', []);
    var statusBox = function (text, offset, width) {
        var box = document.createElement("div");
        box.textContent = text;
        box.style.width = (width - 12) + "px";
        box.style.position = "absolute";
        box.style.bottom = offset + "px";
        box.style.border = "1px solid black";
        box.style.paddingLeft = "5px";
        box.style.paddingRight = "5px";
        return box;
    };
	
	mod.load_image = new Sk.builtin.func(function (image_file) {
        Sk.builtin.pyCheckArgs("load_image", arguments, 1, 1);
        if (!Sk.builtin.checkString(image_file)) {
            throw new Sk.builtin.TypeError("expected string");
        };
        return Sk.misceval.callsim(mod.Image, image_file);
    });
	
	
	mod.grid = new Sk.builtin.func(function(x , y) {
        canvas = document.getElementById("mycanvas");
		context = canvas.getContext('2d');
		for (var x = -500; x < 500; x += 10) {
            context.moveTo(x, -500);
            context.lineTo(x, 500);
        }
		for (var x = -500; x < 500; x += 10) {
            context.moveTo(-500, x);
            context.lineTo(500, x);
        }
		context.stroke();
            
    }); 
	mod.clear_timers = new Sk.builtin.func(function() {
        //cancelAnimation();
	    timers = [];
        for (var i = 1; i < 99999; i++)
            window.clearInterval(i);
    });

    mod.clear = new Sk.builtin.func(function() {
        
        canvas = document.getElementById("mycanvas");        
        context = canvas.getContext('2d');
        
		context.clearRect(0, 0, canvas.width, canvas.height);
        var w = canvas.width;
        canvas.width = 1;
        canvas.width = w;

        context.fillStyle = '#EEEEEE';
        context.fillRect(0, 0, canvas.width, canvas.height);
        //Box
        context.strokeStyle = '#000000';
        context.strokeRect(1,  1, canvas.width-2, canvas.height-2);

		//context.fillStyle = 'white';
		//context.clearRect(0, 0, canvas.width, canvas.height);
        //context.clearRect(-canvas.width, -canvas.height, canvas.width, canvas.height);
        //context.fillRect(0, 0, canvas.width, canvas.height);
		//context.fillRect(-canvas.width, -canvas.height, canvas.width, canvas.height);
    }); 
	
	mod.draw_image = new Sk.builtin.func(function(image, orig_pos, orig_size, final_pos, final_size, rot) {
      
	     
	    
        var sourceX = orig_pos.v[0].v;
		var sourceY = orig_pos.v[1].v;
		var sourceWidth = orig_size.v[0].v;
        var sourceHeight = orig_size.v[1].v;
		
		var destX = final_pos.v[0].v;
		var destY = final_pos.v[1].v;
		var destWidth = final_size.v[0].v;
        var destHeight = final_size.v[1].v;
		var rot = rot.v;
        rot = rot * (2 * Math.PI) / 360.0 

        sourceX = truncate(sourceX - sourceWidth / 2);
        sourceY = truncate(sourceY - sourceHeight / 2);
        var dstoffx = truncate(-destWidth / 2);
        var dstoffy = truncate(-destHeight / 2);

		canvas = document.getElementById("mycanvas");
	    context = canvas.getContext('2d');
        context.save();
        context.translate(destX,destY);
		context.rotate(rot);
		context.drawImage(image.image, sourceX, sourceY, sourceWidth, sourceHeight, dstoffx, dstoffy, destWidth, destHeight);
                                         
		context.restore();
	
		
	});

    mod.draw_text = new Sk.builtin.func(function (text, point, size, color, face) {
            Sk.builtin.pyCheckArgs("draw_text", arguments, 4, 5);
            if (!Sk.builtin.checkString(text)) {
                throw new Sk.builtin.TypeError("text must be a string");
            };
            if (!checkPoint(point)) {
                throw new Sk.builtin.TypeError("point must be a 2 element sequence");
            };
            if (!Sk.builtin.checkNumber(size)) {
                throw new Sk.builtin.TypeError("size must be a number");
            };
            size = Sk.builtin.asnum$(size);
            if (!Sk.builtin.checkString(color)) {
                throw new Sk.builtin.TypeError("color must be a string");
            };
            if (face !== undefined) {
                if (!Sk.builtin.checkString(face)) {
                    throw new Sk.builtin.TypeError("font face must be a string");
                };
                face = Sk.ffi.unwrapo(face); // check if face is valid
                if (fontfaces[face] !== true) {
                    throw new Sk.builtin.ValueError("'" + face + "' is not a valid font face");
                };
            } else { // Default value: serif
                face = "serif";
            };
            canvas = document.getElementById("mycanvas");
		    context = canvas.getContext('2d');
            context.font = size + "px " + face;
            context.fillStyle = Sk.ffi.unwrapo(color);
            text = Sk.ffi.unwrapo(text);
            // Disallow non-printing characters
            //if (textRE.test(text)) {
                //throw new Sk.builtin.ValueError("text may not contain non-printing characters");
            //};
            context.fillText(text,
                Sk.builtin.asnum$(point.mp$subscript(0)),
                Sk.builtin.asnum$(point.mp$subscript(1)));
            return Sk.builtin.none.none$;
     });

    mod.draw_text2 = new Sk.builtin.func(function(a,b,text) {
        canvas = document.getElementById("mycanvas");
		context = canvas.getContext('2d');
        context.fillStyle = "blue";
        context.font = "bold 16px Arial";
        text = Sk.ffi.unwrapo(text);
        context.fillText(text, a.v - 3,b.v);
    });

    mod.draw_polyline = new Sk.builtin.func(function (points, width, color) {
            Sk.builtin.pyCheckArgs("draw_polyline", arguments, 3, 4);
            if (!Sk.builtin.checkSequence(points)) {
                throw new Sk.builtin.TypeError("points must be a sequence");
            };
            if (!Sk.builtin.checkNumber(width)) {
                throw new Sk.builtin.TypeError("width must be a number");
            };
            width = Sk.builtin.asnum$(width);
            if (width <= 0) {
                throw new Sk.builtin.ValueError("width must be a positive number");
            };
            if (!Sk.builtin.checkString(color)) {
                throw new Sk.builtin.TypeError("color must be a string");
            };
            canvas = document.getElementById("mycanvas");
		    context = canvas.getContext('2d');
            context.lineWidth = width;
            context.strokeStyle = Sk.ffi.unwrapo(color);
            context.beginPath();
            var point = points.mp$subscript(0);
            if (!checkPoint(point)) {
                throw new Sk.builtin.TypeError("each point in points must be a 2 element sequence");
            };
            context.moveTo(Sk.builtin.asnum$(point.mp$subscript(0)),
                Sk.builtin.asnum$(point.mp$subscript(1)));
            for (i = 1; i < points.sq$length(); i++) {
                point = points.mp$subscript(i);
                if (!checkPoint(point)) {
                    throw new Sk.builtin.TypeError("each point in points must be a 2 element sequence");
                };
                context.lineTo(Sk.builtin.asnum$(point.mp$subscript(0)),
                    Sk.builtin.asnum$(point.mp$subscript(1)));
            }
            context.stroke();
            return Sk.builtin.none.none$;
        });
        

    mod.draw_circle = new Sk.builtin.func(function (center, radius, linewidth, linecolor, fillcolor) {
        
			       
            Sk.builtin.pyCheckArgs("draw_circle", arguments, 5, 6);
            if (!checkPoint(center)) {
                throw new Sk.builtin.TypeError("center must be a 2 element sequence");
            };
            if (!Sk.builtin.checkNumber(radius)) {
                throw new Sk.builtin.TypeError("radius must be a number");
            };
            radius = Sk.builtin.asnum$(radius);
            if (radius <= 0) {
                throw new Sk.builtin.ValueError("radius must be a positive number");
            };
            if (!Sk.builtin.checkNumber(linewidth)) {
                throw new Sk.builtin.TypeError("linewidth must be a number");
            };
            linewidth = Sk.builtin.asnum$(linewidth);
            if (linewidth <= 0) {
                throw new Sk.builtin.ValueError("linewidth must be a positive number");
            };
            if (!Sk.builtin.checkString(linecolor)) {
                throw new Sk.builtin.TypeError("linecolor must be a string");
            };
            // Check if fillcolor was specified and it is not None
            if ((fillcolor !== undefined) && (fillcolor !== Sk.builtin.none.none$)) {
                if (!Sk.builtin.checkString(fillcolor)) {
                    throw new Sk.builtin.TypeError("fillcolor must be a string");
                };
            } else { // Default value: no fill - fillcolor is None
                fillcolor = Sk.builtin.none.none$;
            };
            
			canvas = document.getElementById("mycanvas");
			context = canvas.getContext('2d');
			context.lineWidth = linewidth;
            context.strokeStyle = Sk.ffi.unwrapo(linecolor);
            if (fillcolor !== Sk.builtin.none.none$) {
                context.fillStyle = Sk.ffi.unwrapo(fillcolor);
            };
            context.beginPath();
            context.arc(Sk.builtin.asnum$(center.mp$subscript(0)),
                Sk.builtin.asnum$(center.mp$subscript(1)), radius, 0, 2 * Math.PI, false);
            if (fillcolor !== Sk.builtin.none.none$) {
                context.fill();
            };
            context.stroke();
            return Sk.builtin.none.none$;
        });

    mod.draw_line2 = new Sk.builtin.func(function(a,b,c,d) {
        canvas = document.getElementById("mycanvas");
		context = canvas.getContext('2d');
		
		//context.beginPath();
        context.moveTo(a.v,b.v);
        context.lineTo(c.v,d.v);
       	//context.closePath();
		//context.fillStyle = 'red';
        context.stroke();
    
    });

    mod.draw_line = new Sk.builtin.func(function (pt1, pt2, width, color) {
            Sk.builtin.pyCheckArgs("draw_line", arguments, 4, 5);
            if (!checkPoint(pt1)) {
                throw new Sk.builtin.TypeError("point1 must be a 2 element sequence");
            };
            if (!checkPoint(pt2)) {
                throw new Sk.builtin.TypeError("point2 must be a 2 element sequence");
            };
            if (!Sk.builtin.checkNumber(width)) {
                throw new Sk.builtin.TypeError("width must be a number");
            }
            width = Sk.builtin.asnum$(width);
            if (width <= 0) {
                throw new Sk.builtin.ValueError("width must be a positive number");
            };
            if (!Sk.builtin.checkString(color)) {
                throw new Sk.builtin.TypeError("color must be a string");
            };
			canvas = document.getElementById("mycanvas");
		    context = canvas.getContext('2d');
            context.lineWidth = width;
            context.strokeStyle = Sk.ffi.unwrapo(color);
            context.beginPath();
            context.moveTo(Sk.builtin.asnum$(pt1.mp$subscript(0)),
                Sk.builtin.asnum$(pt1.mp$subscript(1)));
            context.lineTo(Sk.builtin.asnum$(pt2.mp$subscript(0)),
                Sk.builtin.asnum$(pt2.mp$subscript(1)));
            context.stroke();
            return Sk.builtin.none.none$;
        });

    mod.add_button = new Sk.builtin.func(function (text, handler, width) {
            Sk.builtin.pyCheckArgs("add_button", arguments, 2, 3);
            if (!Sk.builtin.checkString(text)) {
                throw new Sk.builtin.TypeError("text must be a string");
            };
            if (!Sk.builtin.checkFunction(handler)) {
                throw new Sk.builtin.TypeError("handler must be a function");
            };
            if (width !== undefined) {
                if (!Sk.builtin.checkInt(width)) {
                    throw new Sk.builtin.TypeError("width must be an integer");
                };
                width = Sk.builtin.asnum$(width);
            };
            var lineno = Sk.currLineNo;
            // Make the actual button
            var button = document.createElement("button");
            	
            button.type = "button";
            button.textContent = Sk.ffi.unwrapo(text);
            if (width !== undefined) {
                button.style.width = width + "px";
            };
            button.onclick = function () {
                try {
                    var txt = Sk.ffi.basicwrap(button.textContent);
                    Sk.setExecStartNow(true);
                    Sk.currLineNo = lineno;
                    Sk.misceval.callsim(handler, txt);
                    // Give the canvas back the focus
                    $("#mycanvas").focus();
                } catch (e) {
                    Sk.error(e);
                }
            }; // Add button to button zone
            var span = document.createElement("span");
			span.appendChild(button)
			$("#boutons").append(span);
            
            //return Sk.builtin.none.none$;
            return Sk.misceval.callsim(mod.Control, button);
        });

    mod.add_label = new Sk.builtin.func(function (text, width) {
            Sk.builtin.pyCheckArgs("add_label", arguments, 1, 2);
            if (!Sk.builtin.checkString(text)) {
                throw new Sk.builtin.TypeError("text must be a string");
            };
            if (width !== undefined) {
                if (!Sk.builtin.checkInt(width)) {
                    throw new Sk.builtin.TypeError("width must be an integer");
                };
                width = Sk.builtin.asnum$(width);
            };
            // Make the actual label
            var label = document.createElement("span");
            var br = document.createElement("br");
            label.textContent = Sk.ffi.unwrapo(text);
            label.style.display = "inline-block";
            if (width !== undefined) {
                label.style.width = width + "px";
            }; // console.log(label.style);            // Add label to control area
            $("boutons").append(label);
			//return Sk.builtin.none.none$;
            return Sk.misceval.callsim(mod.Control, label);
        });
    mod.add_input = new Sk.builtin.func(function (text, handler, width) {
            Sk.builtin.pyCheckArgs("add_input", arguments, 3, 3);
            if (!Sk.builtin.checkString(text)) {
                throw new Sk.builtin.TypeError("text must be a string");
            };
            if (!Sk.builtin.checkFunction(handler)) {
                throw new Sk.builtin.TypeError("handler must be a function");
            };
            if (!Sk.builtin.checkInt(width)) {
                throw new Sk.builtin.TypeError("width must be an integer");
            };
            width = Sk.builtin.asnum$(width);
            var lineno = Sk.currLineNo;
            // Make the actual text field
            var label = document.createElement("span");
            var textField = document.createElement("textarea");
            var br1 = document.createElement("br");
            var br2 = document.createElement("br");
            label.textContent = Sk.ffi.unwrapo(text);
            textField.rows = 1;
            textField.style.resize = "none";
            textField.style.width = width + "px";

            // Keypress handler to trap "enter" key
            textField.onkeypress = function (evt) { // Call Python handler when "enter" is pressed
                if (evt.keyCode == 13) { // Don't let the text box contain multiple lines
                    evt.preventDefault();
                    try {
                        var txt = Sk.ffi.basicwrap(textField.value);
                        Sk.setExecStartNow(true);
                        Sk.currLineNo = lineno;
                        Sk.misceval.callsim(handler, txt); // Give the canvas back the focus
                        $("#mycanvas").focus();
                    } catch (e) {
                        Sk.error(e);
                    }
                };
            };
          // Add text field to control area
            $("#boutons").append(label);
            $("#boutons").append(br1);
            $("#boutons").append(textField);
            $("#boutons").append(br2);
            return Sk.misceval.callsim(mod.TextAreaControl, textField);
			//return Sk.builtin.none.none$;
        });

    mod.add_checkbox = new Sk.builtin.func(function (id, text,handler, width) {
            Sk.builtin.pyCheckArgs("add_checkbox", arguments, 3, 4);
            if (!Sk.builtin.checkString(id)) {
                throw new Sk.builtin.TypeError("id must be a string");
            };
			if (!Sk.builtin.checkString(text)) {
                throw new Sk.builtin.TypeError("text must be a string");
            };
			if (!Sk.builtin.checkFunction(handler)) {
                throw new Sk.builtin.TypeError("handler must be a function");
            };
            if (width !== undefined) {
                if (!Sk.builtin.checkInt(width)) {
                    throw new Sk.builtin.TypeError("width must be an integer");
                };
                width = Sk.builtin.asnum$(width);
            };
            var lineno = Sk.currLineNo;
            // Make the actual button
            var button = document.createElement("input");
            var br= document.createElement("br");
            button.id = Sk.ffi.unwrapo(id);	
            button.type = "checkbox";
            
            if (width !== undefined) {
                button.style.width = width + "px";
            };
            button.onclick = function (data) {
                try {
                    var txt = Sk.ffi.basicwrap(button.checked);
					Sk.setExecStartNow(true);
                    Sk.currLineNo = lineno;
                    Sk.misceval.callsim(handler, text, txt);
                    // Give the canvas back the focus
                    $("#mycanvas").focus();
                } catch (e) {
                    Sk.error(e);
                }
            }; // Add button to button zone
            var span = document.createElement("span");
            var label = document.createElement("label");
            
            label.htmlFor = Sk.ffi.unwrapo(id);
            label.innerHTML = Sk.ffi.unwrapo(text); 
			span.appendChild(label)
			span.appendChild(button)
			$("#boutons").append(span);
            
            //return Sk.builtin.none.none$;
            return Sk.misceval.callsim(mod.Control, button);
        });

    mod.add_button2 = new Sk.builtin.func(function(a,b,c,d,text) {
        canvas = document.getElementById("mycanvas");
		context = canvas.getContext('2d');
		
		context.beginPath();
        context.moveTo(a.v,b.v);
        context.lineTo(a.v+c.v,b.v);
        context.lineTo(a.v+c.v,b.v+d.v);
        context.lineTo(a.v,b.v+d.v);
        context.closePath();
		context.fillStyle = '#cccccc';
        context.fill();
        
        context.beginPath();
        context.moveTo(a.v,b.v);
        context.lineTo(a.v+c.v,b.v);
        context.lineTo(a.v+c.v,b.v+d.v);
        context.lineTo(a.v,b.v+d.v);
        context.closePath();
		context.strokeStyle = 'black';
        context.stroke();

		context.fillStyle = "blue";
        context.font = "bold 16px Arial";
        text = Sk.ffi.unwrapo(text);
        context.fillText(text, a.v + (c.v / 2) - 6, b.v + (d.v / 2.0) + 6);
        
    });
	mod.fill_rect = new Sk.builtin.func(function(a,b,c,d) {
        canvas = document.getElementById("mycanvas");
		context = canvas.getContext('2d');
		
		context.beginPath();
        context.moveTo(a.v,b.v);
        context.lineTo(a.v+c.v,b.v);
        context.lineTo(a.v+c.v,b.v+d.v);
        context.lineTo(a.v,b.v+d.v);
        context.closePath();
		context.fillStyle = 'Purple';
        context.fill();
    
        
    });
	
	var timer = function ($gbl, $loc) {
        $loc.__init__ = new Sk.builtin.func(function (self, interval, handler) { // Initialize
            self.interval = interval;
            self.handler = handler;
            self._timer = null;
            self.lineno = Sk.currLineNo;
            // Store timer
            timers.push(self);
        });
        $loc.start = new Sk.builtin.func(function (self) {
            Sk.builtin.pyCheckArgs("start", arguments, 1, 1);
            if (self._timer) { // Already running, ignore
                return;
            } // Create new Javascript timer which calls the Python handler
            self._timer = setInterval(function () {
                try {
                    Sk.setExecStartNow(true);
                    Sk.currLineNo = self.lineno;
                    Sk.misceval.callsim(self.handler);
                } catch (e) {
                    clearInterval(self._timer);
                    self._timer = null;
                    Sk.error(e);
                };
            }, Sk.builtin.asnum$(self.interval));
            return Sk.builtin.none.none$;
        });
        $loc.stop = new Sk.builtin.func(function (self) {
            Sk.builtin.pyCheckArgs("stop", arguments, 1, 1);
            // If a Javascript timer exists, stop it and delete it
            if (self._timer) {
                clearInterval(self._timer);
                self._timer = null;
            }
            return Sk.builtin.none.none$;
        });
        $loc.get_interval = new Sk.builtin.func(function (self) {
            Sk.builtin.pyCheckArgs("get_interval", arguments, 1, 1);
            return self.interval;
        });
        $loc.is_running = new Sk.builtin.func(function (self) {
            Sk.builtin.pyCheckArgs("is_running", arguments, 1, 1);
            if (self._timer) {
                return Sk.builtin.bool.true$;
            } else {
                return Sk.builtin.bool.false$;
            }
        });
    };
    mod.Timer = Sk.misceval.buildClass(mod, timer, 'Timer', []);
    mod.create_timer = new Sk.builtin.func(function (interval, handler) {
        Sk.builtin.pyCheckArgs("create_timer", arguments, 2, 2);
        if (!Sk.builtin.checkNumber(interval)) {
            throw new Sk.builtin.TypeError("interval must be a number");
        };
        if (!Sk.builtin.checkFunction(handler)) {
            throw new Sk.builtin.TypeError("handler must be a function");
        };
        if (Sk.builtin.asnum$(interval) <= 0) {
            throw new Sk.builtin.ValueError("interval must be > 0");
        };
        return Sk.misceval.callsim(mod.Timer, interval, handler);
    });
	
    mod.set_draw_handler = new Sk.builtin.func(function (handler) {
            Sk.builtin.pyCheckArgs("set_draw_handler", arguments, 1, 1);
            if (!Sk.builtin.checkFunction(handler)) {
                throw new Sk.builtin.TypeError("handler must be a function");
            };
            draw_handler = handler;
            draw_lineno = Sk.currLineNo;
            return Sk.builtin.none.none$;
        });
    mod.start = new Sk.builtin.func(function (backcolor) {

            Sk.builtin.pyCheckArgs("start", arguments, 0, 1);
			if (!Sk.builtin.checkString(backcolor)) {
                throw new Sk.builtin.TypeError("text must be a string");
            };
            if ((backcolor !== undefined) && (backcolor !== Sk.builtin.none.none$)) {
                if (!Sk.builtin.checkString(backcolor)) {
                    throw new Sk.builtin.TypeError("backcolor must be a string");
                };
            } else { // Default value: no fill - fillcolor is None
                backcolor = Sk.builtin.none.none$;
            };
            
			
            
            // Make the frame visible and start the gui
            canvas = document.getElementById("mycanvas");
		    var context = canvas.getContext('2d');
            if (!context || !context.drawImage) {
                alert("Cannot draw on canvas!");
                return;
            };
            
            // Functions for built-in browser animation callback
            var draw = function () {
                if (backcolor !== Sk.builtin.none.none$) {
					context.fillStyle = Sk.ffi.unwrapo(backcolor);
				} else {
					context.fillStyle = 'Black';
				};
                context.fillRect(0, 0, canvas.width, canvas.height);
                try {
                    Sk.setExecStartNow(true);
                    Sk.currLineNo = draw_lineno;
                    Sk.misceval.callsim(draw_handler, canvas);
                } catch (e) {
                    Sk.error(e);
                }
            };
            var animate = function animate() {
                
                self.animationID = requestAnimationFrame(animate);
                draw();
            };
            // Make sure callbacks stop when window is closed
            window.onbeforeunload = function () { // Works for Chrome and FireFox
                cancelAnimation();
            };
            window.onunload = function () { // Needed for Safari
                cancelAnimation();
            };
            // Request first animation frame
            animationID = requestAnimationFrame(animate);
            return Sk.builtin.none.none$;
        });

	return mod;
}
