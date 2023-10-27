import { useState } from 'react';

function Square({ selected, value, onSquareClick }) {
  return (
    <button style = {{background: selected ? 'rgb(255,0,0)': '#fff'}} className="square" onClick={onSquareClick}>
      {value}
    </button>
  );
}

function Board({ xIsNext, squares, onPlay, moveNumber }) {
  const [squareSelected, setSquareSelected] = useState(-1)
  function handleClick(i) {
    const nextSquares = squares.slice();

    if(moveNumber < 6) {
      if (calculateWinner(squares) || squares[i]) {
        return;
      }
      
      if (xIsNext) {
        nextSquares[i] = 'X';
      } else {
        nextSquares[i] = 'O';
      }
    } else {
      
      if(calculateWinner(squares)) {
        return;
      }

      if (xIsNext) {
        
        if(squareSelected == -1) {
          if(squares[i] == 'X') {
            
            setSquareSelected(i);
          }
          return;

        } else {
          if (i == squareSelected){
            setSquareSelected(-1);
            return;
          }


          if(squares[i] == null && Math.abs((squareSelected % 3) - (i%3)) <= 1 && Math.abs(squareSelected - i) <= 4) {
            nextSquares[i] = 'X';
            nextSquares[squareSelected] = null;
            if (squares[4] == 'X' && squareSelected != 4 && !calculateWinner(nextSquares)){
              alert('Vacate the error spot')
              setSquareSelected(-1);

              return;
            }

            setSquareSelected(-1);
          } else {
            return;
          }
        }

      } else {

        if(squareSelected == -1) {
          if(squares[i] == 'O') {
            setSquareSelected(i);
          }
          return;
        } else {
          if (i == squareSelected){
            setSquareSelected(-1);
            return;
          }

          if(squares[i] == null && Math.abs((squareSelected % 3) - (i%3)) <= 1 && Math.abs(squareSelected - i) <= 4) {
            nextSquares[i] = 'O';
            nextSquares[squareSelected] = null;
            setSquareSelected(-1);
          } else {
            return;
          }
        }

      }


    }
    
    onPlay(nextSquares);
  }

  const winner = calculateWinner(squares);
  let status;
  if (winner) {
    status = 'Winner: ' + winner;
  } else {
    status = 'Next player: ' + (xIsNext ? 'X' : 'O');
  }

  return (
    <>
      <div className="status">{status}</div>
      <div className="board-row">
        <Square selected={squareSelected==0} value={squares[0]} onSquareClick={() => handleClick(0)} />
        <Square selected={squareSelected==1} value={squares[1]} onSquareClick={() => handleClick(1)} />
        <Square selected={squareSelected==2} value={squares[2]} onSquareClick={() => handleClick(2)} />
      </div>
      <div className="board-row">
        <Square selected={squareSelected==3} value={squares[3]} onSquareClick={() => handleClick(3)} />
        <Square selected={squareSelected==4} value={squares[4]} onSquareClick={() => handleClick(4)} />
        <Square selected={squareSelected==5} value={squares[5]} onSquareClick={() => handleClick(5)} />
      </div>
      <div className="board-row">
        <Square selected={squareSelected==6} value={squares[6]} onSquareClick={() => handleClick(6)} />
        <Square selected={squareSelected==7} value={squares[7]} onSquareClick={() => handleClick(7)} />
        <Square selected={squareSelected==8} value={squares[8]} onSquareClick={() => handleClick(8)} />
      </div>
    </>
  );
}

export default function Game() {
  const [history, setHistory] = useState([Array(9).fill(null)]);
  const [currentMove, setCurrentMove] = useState(0);
  const xIsNext = currentMove % 2 === 0;
  const currentSquares = history[currentMove];

  function handlePlay(nextSquares) {
    const nextHistory = [...history.slice(0, currentMove + 1), nextSquares];
    setHistory(nextHistory);
    setCurrentMove(nextHistory.length - 1);
  }

  function jumpTo(nextMove) {
    setCurrentMove(nextMove);
  }

  const moves = history.map((squares, move) => {
    let description;
    if (move > 0) {
      description = 'Go to move #' + move;
    } else {
      description = 'Go to game start';
    }
    return (
      <li key={move}>
        <button onClick={() => jumpTo(move)}>{description}</button>
      </li>
    );
  });

  return (
    <div className="game">
      <div className="game-board">
        <Board xIsNext={xIsNext} squares={currentSquares} onPlay={handlePlay} moveNumber={currentMove} />
      </div>
      <div className="game-info">
        <ol>{moves}</ol>
      </div>
    </div>
  );
}

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
