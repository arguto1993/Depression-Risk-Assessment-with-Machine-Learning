import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.config import DASHBOARD_LINK


@st.cache_data
def load_dashboard_data():
    """Load the dataset for dashboard visualizations."""
    df = pd.read_csv('dataset/Student Depression Dataset.csv')
    return df


def create_donut_chart(df):
    """Create depression distribution donut chart."""
    depression_counts = df['Depression'].value_counts().reset_index()
    depression_counts.columns = ['Depression', 'Count']
    depression_counts['Depression'] = depression_counts['Depression'].map({1: 'Yes', 0: 'No'})
    
    fig = go.Figure(data=[go.Pie(
        labels=depression_counts['Depression'],
        values=depression_counts['Count'],
        hole=0.6,
        marker=dict(colors=['#DC3545', '#28A745']),
        textinfo='label+percent',
        textfont=dict(size=14, color='white'),
        hovertemplate='%{label}<br>Count: %{value}<br>Percent: %{percent}<extra></extra>'
    )])
    
    fig.update_layout(
        title=dict(text='Depression Distribution', font=dict(size=16, color='white')),
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=300,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return fig


def create_grouped_bar_chart(df, x_col, title, x_label):
    """Create grouped bar chart for depression by a categorical variable."""
    grouped_data = df.groupby([x_col, 'Depression']).size().reset_index(name='Count')
    grouped_data['Depression'] = grouped_data['Depression'].map({1: 'Yes', 0: 'No'})
    
    fig = px.bar(
        grouped_data,
        x=x_col,
        y='Count',
        color='Depression',
        barmode='group',
        color_discrete_map={'Yes': '#DC3545', 'No': '#28A745'},
        text='Count'
    )
    
    fig.update_traces(textposition='outside', textfont=dict(size=10))
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color='white')),
        xaxis_title=x_label,
        yaxis_title='Count',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(title='Depression')
    )
    
    return fig


def create_horizontal_bar_chart(df, y_col, title):
    """Create horizontal bar chart for depression by a categorical variable."""
    grouped_data = df.groupby([y_col, 'Depression']).size().reset_index(name='Count')
    grouped_data['Depression'] = grouped_data['Depression'].map({1: 'Yes', 0: 'No'})
    
    fig = px.bar(
        grouped_data,
        y=y_col,
        x='Count',
        color='Depression',
        orientation='h',
        barmode='group',
        color_discrete_map={'Yes': '#DC3545', 'No': '#28A745'},
        text='Count'
    )
    
    fig.update_traces(textposition='outside', textfont=dict(size=10))
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color='white')),
        xaxis_title='Count',
        yaxis_title='',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        height=300,
        margin=dict(l=20, r=20, t=40, b=80),
        legend=dict(title='Depression')
    )
    
    return fig


def create_age_distribution_chart(df):
    """Create age distribution stacked horizontal bar chart."""
    # Create age bins
    age_bins = [0, 18, 21, 24, 28, 33, 100]
    age_labels = ['<18', '18-21', '21-24', '24-28', '28-33', '33+']
    
    df_copy = df.copy()
    df_copy['Age_Group'] = pd.cut(df_copy['Age'], bins=age_bins, 
                                    labels=age_labels, include_lowest=True)
    
    grouped_data = df_copy.groupby(['Age_Group', 'Depression']).size().reset_index(name='Count')
    grouped_data['Depression'] = grouped_data['Depression'].map({1: 'Yes', 0: 'No'})
    
    fig = px.bar(
        grouped_data,
        y='Age_Group',
        x='Count',
        color='Depression',
        orientation='h',
        barmode='stack',
        color_discrete_map={'Yes': '#DC3545', 'No': '#28A745'},
        text='Count'
    )
    
    fig.update_traces(textposition='inside', textfont=dict(size=10, color='white'))
    fig.update_layout(
        title=dict(text='Age Distribution', font=dict(size=16, color='white')),
        xaxis_title='Count',
        yaxis_title='Age',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(title='Depression')
    )
    
    return fig


def create_map_visualization(df):
    """Create map visualization for depression by city."""
    # Get top cities by depression count
    city_data = df[df['City'].isin([
        'Kalyan', 'Hyderabad', 'Srinagar', 'Vasai-Virar', 'Thane', 
        'Kolkata', 'Ludhiana'
    ])].copy()
    
    city_depression = city_data.groupby('City')['Depression'].agg(['sum', 'count']).reset_index()
    city_depression.columns = ['City', 'Depression_Count', 'Total']
    
    # Approximate coordinates for Indian cities
    city_coords = {
        'Kalyan': (19.2403, 73.1305),
        'Hyderabad': (17.3850, 78.4867),
        'Srinagar': (34.0836, 74.7973),
        'Vasai-Virar': (19.4612, 72.7985),
        'Thane': (19.2183, 72.9781),
        'Kolkata': (22.5726, 88.3639),
        'Ludhiana': (30.9010, 75.8573)
    }
    
    city_depression['lat'] = city_depression['City'].map(lambda x: city_coords.get(x, (0, 0))[0])
    city_depression['lon'] = city_depression['City'].map(lambda x: city_coords.get(x, (0, 0))[1])
    
    fig = px.scatter_geo(
        city_depression,
        lat='lat',
        lon='lon',
        size='Depression_Count',
        hover_name='City',
        hover_data={'Depression_Count': True, 'Total': True, 'lat': False, 'lon': False},
        color='Depression_Count',
        color_continuous_scale='Reds',
        size_max=30,
        scope='asia'
    )
    
    fig.update_geos(
        center=dict(lat=23, lon=80),
        projection_scale=4,
        showland=True,
        landcolor='rgb(243, 243, 243)',
        coastlinecolor='rgb(204, 204, 204)',
        showcountries=True,
        countrycolor='rgb(204, 204, 204)'
    )
    
    fig.update_layout(
        title=dict(text='Depression by City', font=dict(size=16, color='white')),
        paper_bgcolor='rgba(0,0,0,0)',
        geo=dict(bgcolor='rgba(0,0,0,0)'),
        font=dict(color='white'),
        height=300,
        margin=dict(l=0, r=0, t=40, b=0),
        coloraxis_colorbar=dict(title='Depression Count')
    )
    
    return fig


def render_dashboard_page():
    """Render the Dashboard page."""
    st.header("Student Depression Dataset")
    
    # Load data
    df = load_dashboard_data()
    
    # Create layout with columns
    # Top row - Record count and filters
    col1, col2, col3 = st.columns([1, 2, 2])
    
    with col1:
        # Record count display
        st.markdown(f"""
            <div style='background-color: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; text-align: center;'>
                <p style='font-size: 14px; margin: 0; color: #888;'>Record Count</p>
                <h1 style='font-size: 48px; margin: 10px 0; color: white;'>{len(df) / 1000:.1f}K</h1>
            </div>
        """, unsafe_allow_html=True)
        
        # Filter section
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Depression**")
        
        # Two checkboxes for Yes and No
        show_yes = st.checkbox("Yes", value=True, key="depression_yes")
        show_no = st.checkbox("No", value=True, key="depression_no")
        
        # Filter data based on checkbox selection
        if show_yes and show_no:
            # Show all data
            filtered_df = df
        elif show_yes:
            # Show only depression=1
            filtered_df = df[df['Depression'] == 1]
        elif show_no:
            # Show only depression=0
            filtered_df = df[df['Depression'] == 0]
        else:
            # Show nothing - create empty dataframe with same structure
            filtered_df = df.head(0)
        
    with col2:
        st.plotly_chart(create_donut_chart(filtered_df), use_container_width=True)
    
    with col3:
        st.plotly_chart(create_grouped_bar_chart(filtered_df, 'Academic Pressure', 
                                                  'Depression by Academic Pressure', 
                                                  'Academic Pressure'), 
                        use_container_width=True)
    
    # Second row
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.plotly_chart(create_map_visualization(filtered_df), use_container_width=True)
    
    with col5:
        st.plotly_chart(create_horizontal_bar_chart(filtered_df, 'Gender', 
                                                     'Depression by Gender'), 
                        use_container_width=True)
    
    with col6:
        st.plotly_chart(create_grouped_bar_chart(filtered_df, 'Financial Stress', 
                                                  'Depression by Financial Stress', 
                                                  'Financial Stress'), 
                        use_container_width=True)
    
    # Third row
    col7, col8, col9 = st.columns(3)
    
    with col7:
        # Get top professions from filtered data
        if len(filtered_df) > 0:
            top_professions = filtered_df['Profession'].value_counts().head(10).index.tolist()
            df_prof = filtered_df[filtered_df['Profession'].isin(top_professions)]
        else:
            df_prof = filtered_df
        st.plotly_chart(create_horizontal_bar_chart(df_prof, 'Profession', 
                                                     'Depression by Profession'), 
                        use_container_width=True)
    
    with col8:
        st.plotly_chart(create_horizontal_bar_chart(filtered_df, 'Have you ever had suicidal thoughts ?', 
                                                     'Thought Suicide?'), 
                        use_container_width=True)
    
    with col9:
        # Get top degrees from filtered data
        if len(filtered_df) > 0:
            top_degrees = filtered_df['Degree'].value_counts().head(10).index.tolist()
            df_degree = filtered_df[filtered_df['Degree'].isin(top_degrees)]
        else:
            df_degree = filtered_df
        st.plotly_chart(create_grouped_bar_chart(df_degree, 'Degree', 
                                                  'Degree Distribution', 
                                                  'Degree'), 
                        use_container_width=True)
    
    # Fourth row - Age distribution
    st.plotly_chart(create_age_distribution_chart(filtered_df), use_container_width=True)
    
    # Add link to original dashboard at the bottom
    st.markdown("---")
    st.markdown(f"**Original Dashboard:** [View on Looker Studio]({DASHBOARD_LINK})")
