import React, { useState } from 'react';
import { Card, CardContent } from '@mui/material';
import { Button } from '@mui/material';

const TriageApp = () => {
  const [formData, setFormData] = useState({
    symptoms: "",
    history: "",
    diagnosis: "",
  });

  const [triageResult, setTriageResult] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();

    // Simulate triage result processing
    const result = {
      level: "Level 1: Resuscitation",
      explanation:
        "The patient's sudden severe headache, difficulty speaking, and weakness on one side of the body are classic symptoms of a stroke, requiring immediate medical attention to prevent further brain damage.",
    };

    setTriageResult(result);
  };

  return (
    <div className="p-6 bg-gray-100 min-h-screen flex flex-col items-center">
      <h1 className="text-2xl font-bold mb-4">Patient Triage Application</h1>
      <Card className="w-full max-w-lg p-4 mb-6">
        <CardContent>
          <form onSubmit={handleSubmit}>
            <div className="mb-4">
              <label className="block text-sm font-medium">Symptoms:</label>
              <textarea
                className="w-full border p-2 rounded"
                value={formData.symptoms}
                onChange={(e) => setFormData({ ...formData, symptoms: e.target.value })}
                required
              />
            </div>

            <div className="mb-4">
              <label className="block text-sm font-medium">Medical History:</label>
              <input
                type="text"
                className="w-full border p-2 rounded"
                value={formData.history}
                onChange={(e) => setFormData({ ...formData, history: e.target.value })}
              />
            </div>

            <div className="mb-4">
              <label className="block text-sm font-medium">Preliminary Diagnosis:</label>
              <input
                type="text"
                className="w-full border p-2 rounded"
                value={formData.diagnosis}
                onChange={(e) => setFormData({ ...formData, diagnosis: e.target.value })}
                required
              />
            </div>

            <Button type="submit" className="w-full">Submit</Button>
          </form>
        </CardContent>
      </Card>

      {triageResult && (
        <Card className="w-full max-w-lg p-4">
          <CardContent>
            <h2 className="text-lg font-bold mb-2">Triage Report</h2>
            <div className="mb-2">
              <strong>Triage Level:</strong> {triageResult.level}
            </div>
            <div>
              <strong>Explanation:</strong> {triageResult.explanation}
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default TriageApp;
