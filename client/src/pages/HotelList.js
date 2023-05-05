import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../CSS/HotelList.css';
import { Link } from 'react-router-dom';
import Nav from '../components/Nav'; 

function HotelList() {
  const [hoteis, setHoteis] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/hoteis').then(response => {
        setHoteis(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);



  return (
    <div className="pt-list">
       <header>
        <Nav /> 
      </header>
      <h1>Hotéis</h1>
      {hoteis.map(hotel => (
        <div className="pt-card" key={hotel.id}>
          <img src={hotel.imagem_url} alt={hotel.name} />
          <div className="card-body">
            <h2>{hotel.name}</h2>
         
            <p>Rating: {hotel.rating}</p>
            <Link to={`/hoteis/${hotel.id}`} className="cta-btn">Ver mais</Link>
          </div>
        </div>
      ))}
    </div>
  );
}

export default HotelList;
