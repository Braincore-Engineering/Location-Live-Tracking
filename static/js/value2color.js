function value2color(value,minvalue=0,maxvalue=10,minColor,maxColor,underMinColor="rgb(155,0,0)",upperMaxColor="rgb(200,250,240)"){
/* Return html color string: rgb(r,g,b).
If value is between minvalue и maxvalue, then the color returns between minColor and maxColor.
If value less them minvalue, then returns underMinColor.
If value more than maxvalue, then returns upperMaxColor.
minColor,maxColor - array [r,g.b] or html color string: rgb(r,g,b), #rrggbb 
*/
function colorStrToArray(colorObj){
	if(Array.isArray(colorObj) && colorObj.length == 3) return colorObj;
	if(typeof colorObj !== "string") return null;
	if(colorObj[0] === '#')	return [parseInt(colorObj.substring(1,3),16), parseInt(colorObj.substring(3,5),16), parseInt(colorObj.substring(5),16)];
	else if (colorObj[0] === 'r') return colorObj.substring(4,colorObj.length-1).split(',').map(str => parseInt(str));
	else return null;
}

minColor = colorStrToArray(minColor) || [255,0,0];	// red
maxColor = colorStrToArray(maxColor) || [0,255,0];	// green

if(value>maxvalue) return upperMaxColor;
if(value<minvalue) return underMinColor;
if(value==minvalue) return `rgb(${minColor[0]},${minColor[1]},${minColor[2]})`;
if(value==maxvalue) return `rgb(${maxColor[0]},${maxColor[1]},${maxColor[2]})`;

const d = (value-minvalue)/Math.abs(maxvalue-minvalue);
let r = Math.round(minColor[0]+(maxColor[0]-minColor[0])*d);
let g = Math.round(minColor[1]+(maxColor[1]-minColor[1])*d);
let b = Math.round(minColor[2]+(maxColor[2]-minColor[2])*d);

return `rgb(${r},${g},${b})`;
} // end function value2color

