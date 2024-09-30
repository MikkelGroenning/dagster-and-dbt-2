with raw_service_requests as (
    select *
    from {{ source('raw_serivce_requests', 'service_requests') }}
)

, final as (
    select 
        name
        , created_date
        , closed_date
        , agency
        , agency_name
        , complaint_type
        , descriptor
        , location_type
        , incident_zip
        , incident_address
        , street_name
        , cross_street_1
        , cross_street_2
        , intersection_street_1
        , intersection_street_
        , address_type
        , cit
        , landmark
        , facility_type
        , status
        , due_date
        , resolution_description
        , resolution_action_updated_date
        , community_board
        , bbl
        , borough
        , x_coordinate_(state_plane)
        , y_coordinate (state_plane)	
        , open_data_channel_type
        , park_facility_name
        , park_borough
        , vehicle_type	
        , taxi_company_borough
        , taxi_pick_up_location
        , bridge_highway_name
        , bridge_highway_direction	
        , road_ramp	
        , bridge_highway_segment	
        , latitude
        , longitude
        , location
    from raw_service_requests
)
select * from final