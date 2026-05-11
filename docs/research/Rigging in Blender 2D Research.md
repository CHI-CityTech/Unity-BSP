The 2 types of rigging in Blender

Cutout Rigging

-Split your character into separate parts (head, torso, arms, legs, eyes)
-Import them as separate images
-Add an armature
-Parent each piece to the bones
-This method is faster
-Great for youtube-style animation
-Has limited bending

https://www.youtube.com/watch?v=oqyW-i32W_0&t=509s

Grease Pencil Rigging
-Draw your character using Grease Pencil
-Add an armature
-Bind the drawing to bones
-Allows smooth bending (not just stiff cutouts)
-More fluid animation
-More natural motion and better for expressive animation
-Slightly harder to set up

Steps in Blender

-Import your file as a SVG (SVG is more ideal than PNG because SVG is a vector file)
-For vector files, shapes are made of curves, not pixels
-SVG is infinitely scalable and editable inside blender 
-Setup bones for each body part
-Parent those body parts to the bones so it’s ready for animation

Rigged body to Unity
-This will work when I export it as FBX to Unity
-It needs to be bone-based rig (armature)
-It must have proper parenting or weights
-It must have keyframed animation (simple transforms)
-Grease pencil rigs not fully supported in Unity
-2D puppet won’t work if it uses complex modifier stacks, procedural node setups and Blender-only constraints (Driver, some IK setups)


I’ve successfully rigged a puppet by following this tutorial instead of the last one

Parent an object to a bone - Blender Tutorial 
Instead of setting parent to armature deform with empty groups, I set it to bone
Ctrl + P > Bone 
