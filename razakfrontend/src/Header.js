import TextLoop from 'react-text-loop'
import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Modal from '@material-ui/core/Modal';
import Backdrop from '@material-ui/core/Backdrop';
import Fade from '@material-ui/core/Fade';



const useStyles = makeStyles((theme) => ({
  modal: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  paper: {
    backgroundColor: theme.palette.background.paper,
    border: '2px solid #000',
    boxShadow: theme.shadows[5],
    padding: theme.spacing(2, 4, 3),
  },
}));


const Header = () => {
  
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (  


    <div className="header">
      {/*<div className="about-us">
      <button type="button" onClick={handleOpen}>
        react-transition-group
      </button>
      <Modal
        aria-labelledby="transition-modal-title"
        aria-describedby="transition-modal-description"
        className={classes.modal}
        open={open}
        onClose={handleClose}
        closeAfterTransition
        BackdropComponent={Backdrop}
        BackdropProps={{
          timeout: 500,
        }}
      >
        <Fade in={open}>
          <div className={classes.paper}>
            <h2 id="transition-modal-title">Transition modal</h2>
            <p id="transition-modal-description">react-transition-group animates me.</p>
          </div>
        </Fade>
      </Modal>
      </div>*/}
      <div className="logo-header">
         <h1>razaknews</h1>
          <p>
             Never miss{"  "}
             <TextLoop>
                <span>News</span>
                <span>Insights</span>
                <span>Intelligence</span>
             </TextLoop>

          </p>
    
      </div>
    
     
     {/* <div className="pages">
        
        <a href='/'>Home</a>
        <a href="/" style={{
          color: "white",
          backgroundColor: '#f1356d',
          borderRadius: '8px'
        }}>About Us</a> 
      </div> */}
    </div>
  );
}
 
export default Header;