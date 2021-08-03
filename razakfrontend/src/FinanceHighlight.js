import React, { useState } from 'react';
import ItemsCarousel from 'react-items-carousel'



const FinanceHighlight = () => {


    const [activeItemIndex, setActiveItemIndex] = useState(0)
    const chevronWidth = 40;
    
    
    
    return ( 
       <div className="finance-highlight">
          <div style={{"padding":"0 60px","maxWidth":"100%","margin":"0 auto"}}>
            <ItemsCarousel
              infiniteLoop={false}
              gutter={12}
              activePosition={'center'}
              chevronWidth={60}
              disableSwipe={false}
              alwaysShowChevrons={true}
              numberOfCards={2}
              slidesToScroll={2}
              outsideChevron={true}
              showSlither={false}
              firstAndLastGutter={false}
              activeItemIndex={activeItemIndex}
              requestToChangeActive={setActiveItemIndex}
              rightChevron={<button>{'>'}</button>}
              leftChevron={<button>{'<'}</button>}
  >
                <div style={{ height: 200, background: '#EEE' }}>First card</div>
                <div style={{ height: 200, background: '#EEE' }}>Second card</div>
                <div style={{ height: 200, background: '#EEE' }}>Third card</div>
                <div style={{ height: 200, background: '#EEE' }}>Fourth card</div>
             </ItemsCarousel>
    </div>
           
       </div>
     );
}
 
export default FinanceHighlight;