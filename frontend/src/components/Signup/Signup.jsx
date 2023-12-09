import React, { useState } from 'react';
import style from './Signup.module.css';

const Signup = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [phone, setPhone] = useState('');

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    // Perform login logic here with username and password
    // For example, you can send an API request or handle authentication logic
    console.log('Login submitted:', username, password, phone);

    // Prepare the data object
    const data = {
      username: username,
      phone: phone,
      password: password
    };

    try {
      // Send the POST request to the server
      const response = await fetch('http://127.0.0.1:8000/user-management/users/', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
          'Content-Type': 'application/json'
        }
      });

      const result = await response.json();
      const token = result["token"]
      localStorage.setItem("token", token)
      alert("Success!")
    } catch (error) {
      // Handle any error that occurred during the request
      console.error('Error:', error);
    }

  };

  return (
    <div className={style.loginContainer}>
      <h2>Sign up</h2>
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
          <label htmlFor="phone">Phone:</label>
          <input
            type="text"
            id="phone"
            value={phone}
            placeholder="09111111111"
            onChange={(event) => setPhone(event.target.value)}
          />
        </div>
        <div className={style.formGroup}>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={handlePasswordChange}
          />
        </div>
        <button type="submit">Sign Up</button>
      </form>
    </div>
  );

};

export default Signup;