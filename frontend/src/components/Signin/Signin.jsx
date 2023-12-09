import React, { useState, useEffect } from 'react';
import style from './Signin.module.css';
import { useNavigate } from 'react-router-dom';

const Signin = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate()

  useEffect(()=>{
    const token = localStorage.getItem("token")

    if (token){
      navigate('/')
    }

  }, [])

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    // Perform login logic here with username and password
    // For example, you can send an API request or handle authentication logic
    console.log(password, username)
    const data = {
        password,
        username
    }

    console.log(data)

    try{

        const res = await fetch("http://localhost:8000/user-management/users/token/",{
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json"
            }
        })

        const token = (await res.json())["token"]
        console.log(token)
        localStorage.setItem("token", token)

    }
    catch (e){

        alert("ERROR")
    }

  };

  return (
    <div className={style.loginContainer}>
      <h2>Sign in</h2>
      <form onSubmit={handleSubmit}>
        <div className={style.formGroup}>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={handleUsernameChange}
          />
        </div>
        <div className={style.formGroup}>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(event)=>setPassword(event.target.value)}
          />
        </div>
        <button type="submit">Sign In</button>
      </form>
    </div>
  );

};

export default Signin;