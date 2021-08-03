import { useState, useEffect } from 'react'
import Malarquee from 'react-malarquee'


const Stocktracker = () => {
  
  
  const [stockprices, setStock] = useState([
    { stockName: '  AAPL ', stockLastHourPrice: 26.59 , id: 0},
    { stockName: ' GOLD ', stockLastHourPrice: 1912.76 , id: 1},
    { stockName: ' COPP ', stockLastHourPrice: 123.1 , id: 2},
    { stockName: ' JJMX ', stockLastHourPrice: 45.67 , id: 3},
    { stockName: ' AMZN ', stockLastHourPrice: 450.78 , id: 4},
    { stockName: ' IBM ', stockLastHourPrice: 10.56 , id: 5},
    { stockName: ' GOOGL ', stockLastHourPrice: 198.00 , id: 6},
    { stockName: ' POHKONG ', stockLastHourPrice: 1.00 , id: 7},
    { stockName: ' ARSTECH ', stockLastHourPrice: 50.46 , id: 8},
  ]);
  

  

  return (  
    <div className="stocktracker" >
    <Malarquee>
     {
       stockprices.map( (stockprice) => (
         <div className="stock-preview" key={ stockprice.id }>
           <span style={{"color":"#ba55d3", "font-weight":"bold"}}>{ stockprice.stockName }:{"  "}</span>
           <span>{"  "}{ stockprice.stockLastHourPrice } {"  "}</span>
         </div>
         
       ))
     }

    </Malarquee>
      
      
    </div>
  );
}
 
export default Stocktracker;

///   <span>{ stockprice.stockName }:{ stockprice.stockLastHourPrice }   {" "}</span>