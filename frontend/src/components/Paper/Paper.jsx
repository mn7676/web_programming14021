import React, { useState, useEffect } from 'react';
import Style from './Paper.module.css'

const Paper = ({gameId}) => {

  const FNAME = "first_name";
  const LNAME = "last_name";
  const CITY = "city";
  const COUNTRY = "country";
  const ANIMAL = "animal";
  const COLOR = "color";

  const [success, setSuccess] = useState({
    [FNAME]: false,
    [LNAME]: false,
    [CITY]: false,
    [COUNTRY]: false,
    [ANIMAL]: false,
    [COLOR]: false
  });

  const handleBlur = (type, value) => {
    if (value == "") return
    // Create the request body object
    const requestBody = {
      type: type,
      value: value
    };
    const token = localStorage.getItem('token')
    // Make the API request to the specified URL
    fetch(`http://localhost:8000/gnames/paper/competition/${gameId}/`, {
      method: 'POST',
      body: JSON.stringify(requestBody),
      headers: {
        'Content-Type': 'application/json',
        "Authorization": `token ${token}`
      }
    })
      .then(response => {
        if (response.ok) {
          // Set the success state for the input type to true
          setSuccess((pre)=>({
            ...pre,
            [type]: true
          }))
        }
      })
      .catch(error => {
        // Handle any errors that occurred during the request
      });
  };

  const renderCircle = type => {
    if (success[type]) {
      return <div className={Style.circleSuccess}></div>;
    } else {
      return <div className={Style.circle}></div>;
    }
  };

  return (
    <div className={Style.paperContainer}>
      <h1>Paper</h1>
      <div className={Style.inputContainer}>
        {renderCircle(FNAME)}
        <input type="text" className={Style.paperInput} placeholder={FNAME} onBlur={(e)=>handleBlur(FNAME, e.target.value)}/>
      </div>
      <div className={Style.inputContainer}>
        {renderCircle(LNAME)}
        <input type="text" className={Style.paperInput} placeholder={LNAME} onBlur={(e)=>handleBlur(LNAME, e.target.value)} />
      </div>
      <div className={Style.inputContainer}>
        {renderCircle(CITY)}
        <input type="text" className={Style.paperInput} placeholder={CITY} onBlur={(e)=>handleBlur(CITY, e.target.value)} />
      </div>
      <div className={Style.inputContainer}>
        {renderCircle(COUNTRY)}
        <input type="text" className={Style.paperInput} placeholder={COUNTRY} onBlur={(e)=>handleBlur(COUNTRY, e.target.value)} />
      </div>
      <div className={Style.inputContainer}>
        {renderCircle(ANIMAL)}
        <input type="text" className={Style.paperInput} placeholder={ANIMAL} onBlur={(e)=>handleBlur(ANIMAL, e.target.value)} />
      </div>
      <div className={Style.inputContainer}>
        {renderCircle(COLOR)}
        <input type="text" className={Style.paperInput} placeholder={COLOR} onBlur={(e)=>handleBlur(COLOR, e.target.value)} />
      </div>
    </div>
  );
};

export default Paper;