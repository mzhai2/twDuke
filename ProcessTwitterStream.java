public void ProcessTwitterStream(InputStream is, String outFilePath) {
BufferedWriter bwrite = null; try {
/** A connection to the streaming API is already * created and the response is contained in
* the InpuStream
*/
JSONTokener jsonTokener = new JSONTokener(new InputStreamReader(is, ‘‘UTF-8’’));
ArrayList <JSONObject > rawtweets = new ArrayList < JSONObject >();
int nooftweetsuploaded = 0;
//Step 1: Read until the stream is exhausted
while(true) { try {
JSONObject temp = new JSONObject(jsonTokener) ;
rawtweets.add(temp);
if (rawtweets.size() >= RECORDS_TO_PROCESS){ Calendar cal = Calendar.getInstance();
String filename = outFilePath + ‘‘tweets_’’ +
cal.getTimeInMillis() + ‘‘.json’’; //Step 2: Periodically write the
processed Tweets to a file
bwrite = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filename), ‘‘UTF -8’’));
nooftweetsuploaded += RECORDS_TO_PROCESS;
for (JSONObject jobj : rawtweets) { bwrite.write(jobj.toString());
bwrite.newLine(); }
bwrite.close(); rawtweets.clear();
}
}
}
}