import React, { useState } from 'react';

const SafeDialSolver = () => {
  const [input, setInput] = useState('');
  const [part1Result, setPart1Result] = useState(null);
  const [part2Result, setPart2Result] = useState(null);
  const [processing, setProcessing] = useState(false);

  const solveDialPuzzle = (instructions) => {
    let position = 50;
    let part1Count = 0; // Count when dial ends at 0
    let part2Count = 0; // Count all times dial points at 0

    const lines = instructions.trim().split('\n');

    for (const line of lines) {
      const direction = line[0];
      const distance = parseInt(line.substring(1));

      if (direction === 'R') {
        // Moving right (toward higher numbers)
        for (let i = 0; i < distance; i++) {
          position = (position + 1) % 100;
          if (position === 0) {
            part2Count++;
          }
        }
      } else if (direction === 'L') {
        // Moving left (toward lower numbers)
        for (let i = 0; i < distance; i++) {
          position = (position - 1 + 100) % 100;
          if (position === 0) {
            part2Count++;
          }
        }
      }

      // Check if we ended at 0 after this rotation (for part 1)
      if (position === 0) {
        part1Count++;
      }
    }

    return { part1: part1Count, part2: part2Count };
  };

  const handleSolve = () => {
    if (!input.trim()) return;

    setProcessing(true);
    setTimeout(() => {
      const results = solveDialPuzzle(input);
      setPart1Result(results.part1);
      setPart2Result(results.part2);
      setProcessing(false);
    }, 100);
  };

  const loadExample = () => {
    const example = `L68
L30
R48
L5
R60
L55
L1
L99
R14
L82`;
    setInput(example);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="bg-slate-800 rounded-lg shadow-2xl p-6 mb-6">
          <h1 className="text-3xl font-bold text-green-400 mb-2">🔐 Safe Dial Solver</h1>
          <p className="text-slate-300 mb-4">Advent of Code - Day 1: Secret Entrance</p>

          <div className="mb-4">
            <label className="block text-slate-300 mb-2 font-semibold">
              Rotation Instructions:
            </label>
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              className="w-full h-48 bg-slate-700 text-green-300 p-3 rounded font-mono text-sm border border-slate-600 focus:border-green-400 focus:outline-none"
              placeholder="Enter rotation instructions (e.g., L68, R48, etc.)"
            />
          </div>

          <div className="flex gap-3 mb-4">
            <button
              onClick={handleSolve}
              disabled={!input.trim() || processing}
              className="bg-green-600 hover:bg-green-700 disabled:bg-slate-600 text-white px-6 py-2 rounded font-semibold transition-colors"
            >
              {processing ? 'Processing...' : 'Solve Puzzle'}
            </button>
            <button
              onClick={loadExample}
              className="bg-purple-600 hover:bg-purple-700 text-white px-6 py-2 rounded font-semibold transition-colors"
            >
              Load Example
            </button>
            <button
              onClick={() => {
                setInput('');
                setPart1Result(null);
                setPart2Result(null);
              }}
              className="bg-slate-600 hover:bg-slate-700 text-white px-6 py-2 rounded font-semibold transition-colors"
            >
              Clear
            </button>
          </div>
        </div>

        {(part1Result !== null || part2Result !== null) && (
          <div className="grid md:grid-cols-2 gap-4">
            <div className="bg-slate-800 rounded-lg shadow-xl p-6 border-2 border-yellow-500">
              <h2 className="text-xl font-bold text-yellow-400 mb-2">⭐ Part 1</h2>
              <p className="text-slate-300 text-sm mb-3">
                Times dial ends at 0 after rotation:
              </p>
              <div className="text-5xl font-bold text-yellow-400">
                {part1Result}
              </div>
            </div>

            <div className="bg-slate-800 rounded-lg shadow-xl p-6 border-2 border-green-500">
              <h2 className="text-xl font-bold text-green-400 mb-2">⭐⭐ Part 2</h2>
              <p className="text-slate-300 text-sm mb-3">
                Total times dial points at 0:
              </p>
              <div className="text-5xl font-bold text-green-400">
                {part2Result}
              </div>
            </div>
          </div>
        )}

        <div className="mt-6 bg-slate-800 rounded-lg shadow-xl p-6">
          <h3 className="text-lg font-bold text-slate-300 mb-3">📋 How it works:</h3>
          <ul className="text-slate-400 space-y-2 text-sm">
            <li>• <strong>Part 1:</strong> Counts only when the dial ends at position 0 after completing a rotation</li>
            <li>• <strong>Part 2:</strong> Counts every time the dial passes through 0, including during rotations</li>
            <li>• The dial starts at position 50</li>
            <li>• L = rotate left (toward lower numbers), R = rotate right (toward higher numbers)</li>
            <li>• The dial wraps around: 0-1 = 99, 99+1 = 0</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default SafeDialSolver;
