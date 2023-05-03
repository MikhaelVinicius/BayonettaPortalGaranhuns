import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './HotelList.css';

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
      <h1>Hoteis</h1>
      {hoteis.map(hotel => (
        <div className="pt-card" key={hotel.id}>
          <img src={hotel.imagem_url} alt={hotel.nome} />
          <div className="card-body">
            <h2>{hotel.nome}</h2>
            <p>{hotel.descricao}</p>
            <p>{hotel.numero_estrelas} estrelas</p>
            <a href="#" className="cta-btn">Ver mais</a>
          </div>
        </div>
      ))}
    </div>
  );
}

export default HotelList;
