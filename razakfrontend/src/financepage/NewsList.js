
import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import { FixedSizeList } from 'react-window';
import { useState, useEffect } from "react";
import ReactList from 'react-list';



const NewsList = () => {

    const [news,setNews] = useState([])

    useEffect(() => {
        fetch('http://localhost:8000/newsapi/api/lead/?format=json')
        .then(response=> response.json())
        .then(data => {
          setNews(data);
        }
         );
      }, [])

      renderRow.propTypes = {
        index: PropTypes.number.isRequired,
        style: PropTypes.object.isRequired,
      };
      
      

    return ( 
      <div className={classes.root}>
      <FixedSizeList height={400} width={300} itemSize={46} itemCount={200}>
        {renderRow}
      </FixedSizeList>
    </div>
     );
}
 
export default NewsList;