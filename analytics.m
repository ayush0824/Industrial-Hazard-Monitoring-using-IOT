% Temperature for the past hour is read from a ThingSpeak channel
% Maximum temperature is written to another ThingSpeak channel.
% Channel ID to read data from
readChannelID = 1297;
% Temperature Field ID
TemperatureFieldID = 4;
% Channel Read API Key
% If your channel is private, then enter the read API
% Key between the ’’ below:
readAPIKey = ’DTATWL0O4KQK6’;
% To store the maximum temperature, write it to a
% channel other than
% the one used for reading data.
writeChannelID = [2554];
% TODO - Enter the Write API Key between the ’’ below:
writeAPIKey = ’Z9PAVI0ERN3G1’;
[tempF, timeStamp] = thingSpeakRead(readChannelID, ’Fields’,
TemperatureFieldID, ’numMinutes’, 60, ’ReadKey’, readAPIKey);
% Calculate the maximum temperature
[maxTempF, maxTempIndex] = max(tempF);
% Choose the timestamp at which the maximum temperature
% was measured
timeMaxTemp = timeStamp(maxTempIndex);
display(maxTempF, ’Maximum Temperature for the last hour is’);
% Write the maximum temperature to another channel specified by
% ’writeChannelID’ variable
display([’Note: To successfully write data to another
channel, ’,...
  ’assign the write channel ID and API Key to
’’writeChannelID’’ and ’,...
’’’writeAPIKey’’ variables above. Also uncomment
the line of code ’,...
’containing ’’thingSpeakWrite’’ (remove ’’%’’ sign
at the beginning of the line.)’])
thingSpeakWrite(writeChannelID, maxTempF, ’timestamp’,
timeMaxTemp, ’Writekey’, writeAPIKey);
