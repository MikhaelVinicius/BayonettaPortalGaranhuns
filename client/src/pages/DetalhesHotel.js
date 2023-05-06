  
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../CSS/DetalhesHotel.css';
import Nav from '../components/Nav'; 

function HotelDetalhes(props) {
  const [hotel, setHotel] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/api/hoteis/${props.match.params.id}`).then(response => {
      setHotel(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, [props.match.params.id]);

  if (!hotel) {
    return <div>Carregando...</div>;
  }

  return (
    <div className="hotel-detalhes">
      <header>
        <Nav /> 
      </header>
      <div className="imagem">
        <img src={hotel.imagem_url} alt={hotel.name} />
      </div>
      <div className="info">
        <h1>{hotel.name}</h1>
        <p>{hotel.address}</p>
        <p>{hotel.city}, {hotel.state}, {hotel.country}</p>
        <p>Rating: {hotel.rating}</p>
        <p>Website: <a href={hotel.website} target="_blank" rel="noreferrer">{hotel.website}</a></p>
        <p>Email: {hotel.email}</p>
        <p>Phone: {hotel.phone}</p>
      </div>
    </div>
  );
}

export default HotelDetalhes;
