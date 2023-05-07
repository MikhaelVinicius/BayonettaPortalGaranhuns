import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../CSS/List.css';
import { Link } from 'react-router-dom';
import Nav from '../components/Nav'; 

function EventosList() {
  const [eventos, setEventos] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/eventos').then(response => {
        setEventos(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  const limitDescription = (descricao) => {
    const limit = 200;
    if (descricao.length <= limit) {
      return descricao;
    } else {
      return descricao.substring(0, limit) + '...';
    }
  };

  return (
    <div className="pt-list">
    <header>
      <Nav /> 
    </header>
    
      <h1>Eventos</h1>
      {eventos.map(eventos => (
        <div className="pt-card" key={eventos.id}>
          <img src={eventos.image_url} alt={eventos.name} />
          <div className="card-body">
            <h2>{eventos.name}</h2>
            <p>{limitDescription(eventos.descricao)}</p>
            <p>{eventos.location}</p>
            <Link to={`/events/${eventos.id}`} className="cta-btn">Ver mais</Link>
          </div>
        </div>
      ))}
    </div>
  );
}

export default EventosList;
