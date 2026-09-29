import { useState } from 'react';
import "./App.css";
import axios from "axios";

function App() {

  const[resume, setResume] = useState(null);
  const[job_description, setJobDescription] = useState("");
  const[response, setResponse] = useState("");
  const[loading, setLoading] = useState(false);

  const handlesubmit = async (e) =>{

    e.preventDefault()

    if  (!resume){
    alert("Resume needs to be uploaded");
    return
    }
      if (!job_description){
      alert("Job description is required");
      return
    }

  const formdata = new FormData()
  formdata.append("resume", resume)
  formdata.append("job_description", job_description)
  
  try{
    setLoading(true);

    const result = await axios.post(
    "https://rag-resume-analysis.rajcloud.blitz.cloud/resume/details/",
    formdata
  );
    // console.log(result.data)
    console.log(result.data.Response)
    setResponse(result.data.Response)
  } catch(error){
    console.log(error);
    setResponse("something went wrong")
  } finally{
    setLoading(false)
  }
};
  
  return (
    <>
    <div className="whole-ui">
      <div className='title'>Resume Analysis

      </div>
      <div className="form-ui">
        <form action="post" onSubmit={handlesubmit}>
          <div>
          <label htmlFor="file-upload">Upload Resume </label>
          <input type="file" id="file-upload"  name='uploaded-file' onChange={(e)=> setResume(e.target.files[0])}/> 
          </div>
          <div>
          <label htmlFor="jd">Job Descritption </label>
          <textarea name="job-description" id="jd" value={job_description} onChange={(e) => setJobDescription(e.target.value)}></textarea>
          </div>
          <div>
          <button type='submit' disabled={loading}>{loading ? "Analyzing the resume..." : "Analyze"}</button>
          </div>
        </form>
      </div>
      <div className='response'>
        <textarea name="backend-respose" id="response-back" value={response} readOnly></textarea>
      </div>
    </div>
    </>
  )
}

export default App
