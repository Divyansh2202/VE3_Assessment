import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from .forms import UploadFileForm
import matplotlib
matplotlib.use('Agg')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_csv(file)

            # Display the first few rows of the data
            data_head = data.head()

            # Calculate summary statistics
            summary_stats = data.describe()

            # Handle missing values
            missing_values = data.isnull().sum().reset_index()
            missing_values.columns = ['Column', 'Missing Values']

            # Generate histograms
            histograms = []
            for column in data.select_dtypes(include=[np.number]).columns:
                plt.figure()
                sns.histplot(data[column].dropna(), kde=True)
                plt.title(f'Histogram for {column}')
                plt.xlabel(column)
                plt.ylabel('Frequency')

                # Save plot to a string buffer
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                string = base64.b64encode(buf.read()).decode('utf-8')
                uri = 'data:image/png;base64,' + string
                histograms.append(uri)
                plt.close()

            context = {
                'data_head': data_head.to_html(),
                'summary_stats': summary_stats.to_html(),
                'missing_values': missing_values.to_html(index=False),
                'histograms': histograms,
            }
            return render(request, 'analysis/results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})
