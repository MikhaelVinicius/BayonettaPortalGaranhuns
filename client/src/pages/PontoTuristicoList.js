import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './PontoTuristicoList.css'; 

function PontoTuristicoList() {
  const [pontosTuristicos, setPontosTuristicos] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/pontos_turisticos').then(response => {
        setPontosTuristicos(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div className="pt-list"> {/* Adicionando a classe pt-list */}
      <h1>Pontos turísticos</h1>
      {pontosTuristicos.map(pontoTuristico => (
        <div className="pt-card" key={pontoTuristico.id}> {/* Adicionando a classe pt-card */}
          <img src={pontoTuristico.imagem_url} alt={pontoTuristico.nome} />
          <div className="card-body"> {/* Adicionando a classe card-body */}
            <h2>{pontoTuristico.nome}</h2>
            <p>{pontoTuristico.descricao}</p>
            <p>{pontoTuristico.localizacao}</p>
            <a href="#" className="cta-btn">Ver mais</a> {/* Adicionando a classe cta-btn */}
          </div>
        </div>
      ))}
    </div>
  );
}

export default PontoTuristicoList;
