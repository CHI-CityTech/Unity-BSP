**Dimensions map:**

**\-There are no such thing as maps for keeping measurements and scaling**  
\-Dimensions are parametric (real data) in fusion 360  
\-Fusion 360 doesn’t use maps for scaling, just parameters and constraints  
\-When importing STEP and IGES files, you get solid geometry   
\-You can’t edit those files for the most part, but I did with a click of a button  
\-You only get the final shape without the sketch history  
\-If you import a F3D file, you can edit it, keep sketch history and dimensions  
\-If you import a OBJ or STL, it only keeps the shape and doesn’t keep the dimensions  
\-Importing to blender, blender sees a shape, not dimensions  
\-Blender is not parametric, so it cant read parametric data importing OBJ, FBX and STL into it

To obtain fusion like control in blender:  
\-You can use geometry nodes for procedural control  
\-Use drivers for numeric relationships

**Workflows to making the stage correct measurements in blender:**  
\-Build everything in fusion 360(with accurate measurements)  
\-Export as OBJ or STEP, then convert to mesh in blender  
\-Then export as an FBX, to take to UNITY

\-Use milliliters in fusion 360  
\-In blender, set unit system to Metric, then Unit scale to 0.001, then select object\>CTRL \+ A\>Apply scale  
\-Unity uses meters

**Before exporting to FBX make sure to:**  
\-Apply scale and rotation  
\-Set origin points correctly  
\-Keep hierarchy clean

\-Fusion exports in mm  
\-Blender assumes meters  
\-Blender will preserve scaling and lets you measure

**Maps that blender use:**  
\-Displacement map  
\-Normal map  
\-Roughness map  
\-UV map  
\-Metallic map

**Importing OBJ room to blender:**  
\-I brought the 3D room model I created from fusion to blender and the sceneview is choppy  
\-I changed the view clipping to a bigger number but the model looks distorted  
\-Blender can’t accurately calculate depth when the model is huge scale and/or the clip end is set to a huge value  
\-But I didn’t have that issue when I imported the room scan to blender   
**\-I fixed it**  
\-I reimported it and scaled it down to 0.001 because it was huge compared to the room model  
\-Went to “OBJECT” underneath the hierarchy and changed it there and looks clear  
\-After changing scale, you apply scale so both models are consistent(CTRL \+ A\<Apply Scale)  
**If you don’t do this last scaling step:**  
\-Unity imports can behave weird  
\-Physics/transforms may break  
\-Parenting/animation inconsistencies  
\-Harder to manage precise transforms  
**\-Blender uses Meters**  
**\-Fusion 360 uses Milliliters**   
**\-Unity uses Meters**

**How to scan capture the t-slot profiles efficiently to bring to the digital:**   
\-Can’t 3D scan shiny, reflective surfaces  
\-Polycam or Scaniverse can’t track features because of the light bounces  
**You can add tracking features by:**  
\-Putting painter’s tape, adding random stickers or marker dots on the physical object  
\-This gives the scanner anchors so it doesn’t lose tracking  
\-You can make it matte by spraying chalk spray, baby powder or dry shampoo  
\-This is what professionals do when scanning metal parts  
**Other alternatives**  
\-You can avoid direct sunlight or harsh reflections  
\-Change lighting by using soft, diffused light  
\-Don’t scan under bright overhead LEDs hitting the metal directly  
\-Move slower when scanning  
\-Start from a corner or intersection  
\-Keep consistent distance  
\-Do multiple passes if needed  
