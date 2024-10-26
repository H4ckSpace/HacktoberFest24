import React from "react"
import "./Home.css"
const Home = () => {
  const wordSet = {
    5: "board",
    6: "kousik",
    7: "nehanth",
    8: "krishnan",
}
const selectedWord = wordSet[numberOfLetters]   // Target Word get selected randomly
  const selectedWordArr = selectedWord.split("")
  
  const handleInput = () => {
    console.log("")
  }

  // Creating input cells 
  const rows = []
    for (let i = 0; i < selectedWordArr.Length + 1; i++) {
        // Rows
        rows.push(
            <div className="input-field" key={i}>
                {/* Columns */}
                {selectedWordArr.map((letter, columnIndex) => (
                    <input
                        type="text"
                        key={columnIndex}
                        id={`${i}-${columnIndex}`}
                        t
                        onChange={(e) => handleInput(e, columnIndex, i)}
                        maxLength={1}
                        disabled={!(i === 0 && columnIndex === 0)}
                        // ref={(el) => (inputRefs.current[columnIndex] = el)}
                        ref={(el) => {
                            inputRefs.current[i] = inputRefs.current[i] || []
                            inputRefs.current[i][columnIndex] = el
                        }}
                    />
                ))}
            </div>
        )
  }
  
  const handleSubmit = () => {
    console.log("");
  }
    return (
        <div className="Home">
            <select name="number_of_letters" id="number_of_letters" onChange={(e) => setNumberOfLetters(e.target.value)}>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
            </select>
            <form className="inputs-field" onSubmit={handleSubmit}>
                {rows}
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default Home
