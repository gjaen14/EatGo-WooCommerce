const fs = require('fs');
const path = require('path');

const data = JSON.parse(fs.readFileSync('clean_native_args.json', 'utf8'));

// We will use standard bash to format this into a call for the AI, or we can just patch the script widget
