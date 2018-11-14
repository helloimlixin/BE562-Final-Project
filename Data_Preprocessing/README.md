<h1>Data Preprocessing</h1>

<h2>File Content</h2>
This folder contains two files:
<ol type="1">
  <li><strong>DataParser.py</strong>: the Python script to read a copy number data file into a numpy array and output a distance matrix using the <strong>Manhattan distance</strong>.</li>
  <li><strong>test.txt</strong>: a test txt file with only the first 10 copy number rows of the original data in the file 
  <code>\breast_cancer_data_filtered\B1\B1_DCIS.txt</code>, where the original Breast Cancer data file is provided in the
  FISH dataset provided in the folder <code>breast_cancer_data_filtered</code>. </li>
</ol>

<h2>Program Execution</h2>
With the <code>test.txt</code> in the same directory as the Python script file <code>DataParser.py</code>, the program can be
executed as follows:

<code align="center">python Dataparser.py</code>

<h2>Program Output</h2>
The Manhattan Distance Matrix (for 10 cell count patterns):
<table>
<thead>
<tr><th style="text-align: right;">  </th><th style="text-align: right;">  0</th><th style="text-align: right;">  1</th><th style="text-align: right;">  2</th><th style="text-align: right;">  3</th><th style="text-align: right;">  4</th><th style="text-align: right;">  5</th><th style="text-align: right;">  6</th><th style="text-align: right;">  7</th><th style="text-align: right;">  8</th><th style="text-align: right;">  9</th></tr>
</thead>
<tbody>
<tr><td style="text-align: right;"> 0</td><td style="text-align: right;">  0</td><td style="text-align: right;">  1</td><td style="text-align: right;">  6</td><td style="text-align: right;">  3</td><td style="text-align: right;">  1</td><td style="text-align: right;">  6</td><td style="text-align: right;">  8</td><td style="text-align: right;">  4</td><td style="text-align: right;">  3</td><td style="text-align: right;">  1</td></tr>
<tr><td style="text-align: right;"> 1</td><td style="text-align: right;">  1</td><td style="text-align: right;">  0</td><td style="text-align: right;">  7</td><td style="text-align: right;">  4</td><td style="text-align: right;">  2</td><td style="text-align: right;">  5</td><td style="text-align: right;">  7</td><td style="text-align: right;">  5</td><td style="text-align: right;">  4</td><td style="text-align: right;">  2</td></tr>
<tr><td style="text-align: right;"> 2</td><td style="text-align: right;">  6</td><td style="text-align: right;">  7</td><td style="text-align: right;">  0</td><td style="text-align: right;">  3</td><td style="text-align: right;">  5</td><td style="text-align: right;"> 12</td><td style="text-align: right;"> 14</td><td style="text-align: right;">  2</td><td style="text-align: right;">  3</td><td style="text-align: right;">  5</td></tr>
<tr><td style="text-align: right;"> 3</td><td style="text-align: right;">  3</td><td style="text-align: right;">  4</td><td style="text-align: right;">  3</td><td style="text-align: right;">  0</td><td style="text-align: right;">  2</td><td style="text-align: right;">  9</td><td style="text-align: right;"> 11</td><td style="text-align: right;">  1</td><td style="text-align: right;">  0</td><td style="text-align: right;">  2</td></tr>
<tr><td style="text-align: right;"> 4</td><td style="text-align: right;">  1</td><td style="text-align: right;">  2</td><td style="text-align: right;">  5</td><td style="text-align: right;">  2</td><td style="text-align: right;">  0</td><td style="text-align: right;">  7</td><td style="text-align: right;">  9</td><td style="text-align: right;">  3</td><td style="text-align: right;">  2</td><td style="text-align: right;">  0</td></tr>
<tr><td style="text-align: right;"> 5</td><td style="text-align: right;">  6</td><td style="text-align: right;">  5</td><td style="text-align: right;"> 12</td><td style="text-align: right;">  9</td><td style="text-align: right;">  7</td><td style="text-align: right;">  0</td><td style="text-align: right;">  2</td><td style="text-align: right;"> 10</td><td style="text-align: right;">  9</td><td style="text-align: right;">  7</td></tr>
<tr><td style="text-align: right;"> 6</td><td style="text-align: right;">  8</td><td style="text-align: right;">  7</td><td style="text-align: right;"> 14</td><td style="text-align: right;"> 11</td><td style="text-align: right;">  9</td><td style="text-align: right;">  2</td><td style="text-align: right;">  0</td><td style="text-align: right;"> 12</td><td style="text-align: right;"> 11</td><td style="text-align: right;">  9</td></tr>
<tr><td style="text-align: right;"> 7</td><td style="text-align: right;">  4</td><td style="text-align: right;">  5</td><td style="text-align: right;">  2</td><td style="text-align: right;">  1</td><td style="text-align: right;">  3</td><td style="text-align: right;"> 10</td><td style="text-align: right;"> 12</td><td style="text-align: right;">  0</td><td style="text-align: right;">  1</td><td style="text-align: right;">  3</td></tr>
<tr><td style="text-align: right;"> 8</td><td style="text-align: right;">  3</td><td style="text-align: right;">  4</td><td style="text-align: right;">  3</td><td style="text-align: right;">  0</td><td style="text-align: right;">  2</td><td style="text-align: right;">  9</td><td style="text-align: right;"> 11</td><td style="text-align: right;">  1</td><td style="text-align: right;">  0</td><td style="text-align: right;">  2</td></tr>
<tr><td style="text-align: right;"> 9</td><td style="text-align: right;">  1</td><td style="text-align: right;">  2</td><td style="text-align: right;">  5</td><td style="text-align: right;">  2</td><td style="text-align: right;">  0</td><td style="text-align: right;">  7</td><td style="text-align: right;">  9</td><td style="text-align: right;">  3</td><td style="text-align: right;">  2</td><td style="text-align: right;">  0</td></tr>
</tbody>
</table>
