const csv = require('csv-parser');
const fs = require('fs');

/*
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
*/

const texts = [];
const calls = [];

fs.createReadStream('texts.csv')
  .pipe(csv(['incoming', 'answering', 'date_time']))
  .on('data', data => texts.push(data))
  .on('end', () => {
    console.log(
      `First record of texts, ${texts[0].incoming} texts ${
        texts[0].answering
      } at time ${texts[0].date_time.slice(11)}`
    );
  });

fs.createReadStream('calls.csv')
  .pipe(csv(['incoming', 'answering', 'date_time', 'duration']))
  .on('data', data => calls.push(data))
  .on('end', () => {
    console.log(
      `Last record of calls, ${calls[calls.length - 1].incoming} calls ${
        calls[calls.length - 1].answering
      } at time ${calls[0].date_time.slice(11)}, lasting ${
        calls[calls.length - 1].duration
      } seconds`
    );
  });
