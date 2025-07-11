
<template>
  <div>
    <h2>Available Courses</h2>
    <div v-for="course in courses" :key="course.id">
      <h3>{{ course.title }}</h3>
      <button @click="enroll(course.id)">Enroll</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      courses: []
    }
  },
  created() {
    axios.get('/api/courses/').then(res => {
      this.courses = res.data
    })
  },
  methods: {
    enroll(courseId) {
      axios.post('/api/enroll/', { course: courseId })
    }
  }
}
</script>
