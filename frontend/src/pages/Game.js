import Paper from '../components/Paper/Paper';
import StartGame from '../components/StartGame/StartGame';
import React, { useState } from 'react';

const Game = () => {
  const [gameId, setGameId] = useState(null);

  return (
    <div>
      {gameId ? (
        <Paper gameId={gameId} />
      ) : (
        <StartGame setGameId={setGameId} />
      )}
    </div>
  );
};
  
export default Game;