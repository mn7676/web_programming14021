import React, { useState, useEffect } from 'react';
import './StartGame.module.css'

const StartGame = ({ setGameId }) => {


  const generateGameId = async ()=>{

    const token = localStorage.getItem('token')
    const res = await fetch("http://localhost:8000/gnames/participations/",{
      method: "POST",
      headers: {
          "Content-Type": "application/json",
          "Authorization": `Token ${token}`
      }

  })

  const result = (await res.json())
  return result["competition"]
  }

  const handleStartGame = async () => {
    // Generate a new game ID (you can replace this with your own logic)
    const newGameId = await generateGameId();

    // Set the game ID using the setGameId function passed as a prop
    setGameId(newGameId)
  };

  return (
    <div>
      <h1>Start Game</h1>
      <button onClick={handleStartGame}>Start</button>
    </div>
  );
};

export default StartGame;