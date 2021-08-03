import Stocktracker from './Stocktracker'
import FinanceSlider from './FinanceSlider';
import Line from './Divider';





const Finance = () => {
    return (  
        <div className="finance-page">  
          <Stocktracker />
          <div className="finance-first-block">
              <div className="finance-top-news">
                 <FinanceSlider />

                 
              </div>
          </div>
         <Line />
         
          

      </div>
    );
}
 
export default Finance;