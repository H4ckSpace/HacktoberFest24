const http = require('http');
const { JSDOM } = require('jsdom');

// Create a new JSDOM instance
const dom = new JSDOM(`<!DOCTYPE html><html><body></body></html>`);
const document = dom.window.document;

// Create the main container for the calculator
const calculatorContainer = document.createElement('div');
calculatorContainer.style.width = '300px';
calculatorContainer.style.margin = '50px auto';
calculatorContainer.style.padding = '20px';
calculatorContainer.style.border = '2px solid #333';
calculatorContainer.style.borderRadius = '8px';
calculatorContainer.style.textAlign = 'center';
document.body.appendChild(calculatorContainer);

// Display screen for calculator
const screen = document.createElement('input');
screen.type = 'text';
screen.id = 'screen';
screen.style.width = '100%';
screen.style.height = '40px';
screen.style.fontSize = '1.5rem';
screen.style.marginBottom = '10px';
screen.style.textAlign = 'right';
screen.disabled = true;
calculatorContainer.appendChild(screen);

// Buttons layout
const buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
];

// Handle button click
function handleClick(value) {
    const currentScreen = document.getElementById('screen');
    if (value === 'C') {
        currentScreen.value = '';
    } else if (value === '=') {
        try {
            currentScreen.value = eval(currentScreen.value);
        } catch (e) {
            currentScreen.value = 'Error';
        }
    } else {
        currentScreen.value += value;
    }
}

// Generate buttons dynamically
buttons.forEach(row => {
    const rowDiv = document.createElement('div');
    rowDiv.style.display = 'flex';
    rowDiv.style.justifyContent = 'space-around';
    row.forEach(label => {
        const button = document.createElement('button');
        button.textContent = label;
        button.style.width = '20%';
        button.style.height = '40px';
        button.style.fontSize = '1.2rem';
        button.onclick = () => handleClick(label);
        rowDiv.appendChild(button);
    });
    calculatorContainer.appendChild(rowDiv);
});

// Create and start the server
const PORT = 3000; // Specify the port
const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    res.end(dom.serialize()); // Send the entire HTML structure
});

server.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}/`);
});
