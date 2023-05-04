import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './RestauranteList.css';

function RestauranteList() {
  const [restaurantes, setRestaurantes] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/restaurantes').then(response => {
        setRestaurantes(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div className="pt-list">
      <h1>Restaurantes</h1>
      {restaurantes.map(restaurante => (
        <div className="pt-card" key={restaurante.id}>
          <img src={restaurante.imagem_url} alt={restaurante.nome} />
          <div className="card-body">
            <h2>{restaurante.nome}</h2>
            <p>{restaurante.descricao}</p>
            <p>{restaurante.localizacao}</p>
            <a href="#" className="cta-btn">Ver mais</a>
          </div>
        </div>
      ))}
    </div>
  );
}

export default RestauranteList;
