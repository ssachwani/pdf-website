import React, { useState } from 'react';

function App() {
  const [files, setFiles] = useState([]);

  const handleMerge = async () => {
    const formData = new FormData();
    files.forEach(file => formData.append('files', file));

    const response = await fetch('https://pdf-backend.onrender.com/merge', {
      method: 'POST',
      body: formData,
    });

    const data = await response.json();
    window.open(`https://pdf-backend.onrender.com${data.download_link}`, '_blank');
  };

  return (
    <div>
      <h1>PDF Merger</h1>
      <input type="file" multiple onChange={(e) => setFiles([...e.target.files])} />
      <button onClick={handleMerge}>Merge PDFs</button>
    </div>
  );
}

export default App;