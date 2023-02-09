import './App.css';
import { motion, AnimatePresence } from 'framer-motion';

function App() {
  return (
    <AnimatePresence>
      <motion.div
        initial={{ scale: 0.5, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ scale: 0.5, opacity: 0 }}
        transition={{ duration: 0.5 }}
        className="error-container"
      >
        <h1 className="error-title">404</h1>
        <p className="error-text">Sorry, the page you're looking for can't be found</p>
      </motion.div>
    </AnimatePresence>
  );
}

export default App;
