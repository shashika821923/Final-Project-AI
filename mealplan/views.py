from django.http import JsonResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import json
from sklearn.cluster import KMeans

@csrf_exempt
def suggest_meal_plan(request):
    if request.method == 'POST':
        height_cm = float(json.loads(request.body.decode('utf-8'))['height_cm'])
        weight_kg = float(json.loads(request.body.decode('utf-8'))['weight_kg'])

        # Load persons data from CSV using pandas
        persons_df = pd.read_csv('sample.csv')

        # Apply KMeans clustering to generate cluster labels
        model = KMeans(n_clusters=3)  # Adjust cluster count based on data size
        cluster_labels = model.fit_predict(persons_df[['Height_cm', 'Weight_kg']])

        # Add cluster labels to the DataFrame
        persons_df['cluster'] = cluster_labels

        # Save the DataFrame back to CSV (optional, for future use)
        persons_df.to_csv('persons_data_with_clusters.csv', index=False)

        # Predict user's cluster based on height and weight
        predicted_cluster = model.predict([[height_cm, weight_kg]])[0]

        # Filter data for the predicted cluster
        clustered_data = persons_df.loc[persons_df['cluster'] == predicted_cluster]

        # Extract suggested meal plan and recommended foods from similar person
        suggested_meal_plan = clustered_data['Meal_Plan'].iloc[0]  # Replace index selection with your logic
        recommended_foods = clustered_data['Foods'].iloc[0]

        # Return response as JSON
        response_data = {
            'suggested_meal_plan': suggested_meal_plan,
            'recommended_foods': recommended_foods
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
